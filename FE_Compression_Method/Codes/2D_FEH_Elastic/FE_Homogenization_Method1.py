#
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import string
import random
import numpy as np
#
from GeometryShape2D import *
#
executeOnCaeStartup()
#
#------------------------------------------------------------------------------------
#
RLength = 200.0
Filnum, rs = 10, [RLength, 0.0, RLength, 0.0]
mshsize, disp = 0.75, [(rs[0]-rs[1])*0.1, (rs[2]-rs[3])*0.1]
#
for ifil in range(Filnum):
    #
    Mdb()
    #
    session.journalOptions.setValues(replayGeometry=INDEX, recoverGeometry=INDEX)
    #
    caename, pathname, jobname = 'RVE_'+str(ifil+1)+'.cae', 'FE_Model_'+str(ifil+1)+'.cae', 'Job-'+str(ifil+1)
    #
    openMdb(pathName=caename)
    #
    #-------------------------------------------------------------------------------------
    #
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((0.00335, 0.35), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    region = regionToolset.Region(faces=p.faces)
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, offsetType=MIDDLE_SURFACE, 
        offsetField='', thicknessAssignment=FROM_SECTION)
    #
    mdb.models['Model-1'].Material(name='Material-2')
    mdb.models['Model-1'].materials['Material-2'].Elastic(table=((0.074, 0.2), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='Material-2', thickness=None)
    p = mdb.models['Model-1'].parts['Part-2']
    region = regionToolset.Region(faces=p.faces)
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, offsetType=MIDDLE_SURFACE, 
        offsetField='', thicknessAssignment=FROM_SECTION)
    #
    #-------------------------------------------------------------------------------------
    #
    mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-1', previous='Initial')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'U', 'EVOL', 'IVOL'))
    mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-2', previous='Step-1')
    mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-3', previous='Step-2')
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['Part-1-1'], a.instances['Part-2-1'], )
    a.seedPartInstance(regions=partInstances, size=mshsize, deviationFactor=0.1, minSizeFactor=0.1)
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-1-1'].edges
    e = alledges[0:0]
    for iedge in alledges:
        pt = iedge.pointOn[0]
        if abs(pt[1]-rs[3]) < 1.0E-3 or abs(pt[0]-rs[0]) < 1.0E-3 or abs(pt[1]-rs[2]) < 1.0E-3 or abs(pt[0]-rs[1]) < 1.0E-3:
            e += alledges[iedge.index:iedge.index+1]
    a.seedEdgeBySize(edges=e, size=mshsize, deviationFactor=0.1, minSizeFactor=0.1, constraint=FIXED)
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-2-1'].edges
    e = alledges[0:0]
    for iedge in alledges:
        pt = iedge.pointOn[0]
        if abs(pt[1]-rs[3]) < 1.0E-3 or abs(pt[0]-rs[0]) < 1.0E-3 or abs(pt[1]-rs[2]) < 1.0E-3 or abs(pt[0]-rs[1]) < 1.0E-3:
            e += alledges[iedge.index:iedge.index+1]
    a.seedEdgeBySize(edges=e, size=mshsize, deviationFactor=0.1, minSizeFactor=0.1, constraint=FIXED)
    #
    a = mdb.models['Model-1'].rootAssembly
    f = a.instances['Part-1-1'].faces + a.instances['Part-2-1'].faces
    a.setMeshControls(regions=f, elemShape=QUAD)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    a.setElementType(regions=(f, ), elemTypes=(elemType1, elemType2))
    a.generateMesh(regions=(a.instances['Part-1-1'],a.instances['Part-2-1'],))
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-1-1'].edges
    selectedges = alledges[0:0]
    #
    for iedge in alledges:
        pt = iedge.pointOn[0]
        if abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            selectedges += alledges[iedge.index:iedge.index+1]
    #
    a = mdb.models['Model-1'].rootAssembly
    a.Surface(side1Edges=selectedges, name='Master-1')
    a.Set(edges=selectedges, name='Common-Surf-1')
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-2-1'].edges
    selectedges = alledges[0:0]
    for iedge in alledges:
        pt = iedge.pointOn[0]
        if abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            selectedges += alledges[iedge.index:iedge.index+1]
    #
    a = mdb.models['Model-1'].rootAssembly
    a.Surface(side1Edges=selectedges, name='Slave-1')
    #
    a = mdb.models['Model-1'].rootAssembly
    region1, region2 = a.surfaces['Master-1'], a.surfaces['Slave-1']
    mdb.models['Model-1'].Tie(name='Tie-1', master=region2, slave=region1, positionToleranceMethod=COMPUTED, adjust=ON, 
        tieRotations=OFF, thickness=ON)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    allnodes = a.instances['Part-1-1'].nodes
    setnds = a.sets['Common-Surf-1'].nodes
    selcnds = setnds[0:0]
    for isetn in setnds:
        pt = isetn.coordinates
        if abs(pt[0]-rs[0]) < 1.0E-3 or abs(pt[0]-rs[1]) < 1.0E-3 or abs(pt[1]-rs[2]) < 1.0E-3 or abs(pt[1]-rs[3]) < 1.0E-3:
            selcnds += allnodes[isetn.label-1:isetn.label]
    #
    a = mdb.models['Model-1'].rootAssembly
    allnodes = a.instances['Part-1-1'].nodes
    EABnds, EBCnds, ECDnds, EDAnds = allnodes[0:0], allnodes[0:0], allnodes[0:0], allnodes[0:0]
    #
    for inode in allnodes:
        #
        pt = inode.coordinates
        #
        if abs(pt[1]-rs[3]) < 1.0E-3 and abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3:
            if inode not in selcnds:
                EABnds += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[0]) < 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            if inode not in selcnds:
                EBCnds += allnodes[inode.label-1:inode.label]
        if abs(pt[1]-rs[2]) < 1.0E-3 and abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3:
            if inode not in selcnds:
                ECDnds += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[1]) < 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            if inode not in selcnds:
                EDAnds += allnodes[inode.label-1:inode.label]
    #
    for i in range(len(EABnds)):
        setname1 = 'Edge-AB-' + str(i+1)
        setname2 = 'Edge-CD-' + str(i+1)
        a = mdb.models['Model-1'].rootAssembly
        a.Set(nodes=(EABnds[i:i+1], ), name=setname1)
        #
        for j in range(len(ECDnds)):
            dist = EABnds[i].coordinates[0] - ECDnds[j].coordinates[0]
            if abs(dist) < 1.0E-4:
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=(ECDnds[j:j+1], ), name=setname2)
    #
    for i in range(len(EBCnds)):
        setname1 = 'Edge-BC-' + str(i+1)
        setname2 = 'Edge-DA-' + str(i+1)
        a = mdb.models['Model-1'].rootAssembly
        a.Set(nodes=(EBCnds[i:i+1], ), name=setname1)
        #
        for j in range(len(EDAnds)):
            dist = EBCnds[i].coordinates[1] - EDAnds[j].coordinates[1]
            if abs(dist) < 1.0E-4:
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=(EDAnds[j:j+1], ), name=setname2)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    allnodes = a.instances['Part-2-1'].nodes
    EABnds1, EBCnds1, ECDnds1, EDAnds1 = allnodes[0:0], allnodes[0:0], allnodes[0:0], allnodes[0:0]
    #
    for inode in allnodes:
        pt = inode.coordinates
        #
        if abs(pt[1]-rs[3]) < 1.0E-3 and abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3:
            EABnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[0]) < 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            EBCnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[1]-rs[2]) < 1.0E-3 and abs(pt[0]-rs[0]) > 1.0E-3 and abs(pt[0]-rs[1]) > 1.0E-3:
            ECDnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[1]) < 1.0E-3 and abs(pt[1]-rs[2]) > 1.0E-3 and abs(pt[1]-rs[3]) > 1.0E-3:
            EDAnds1 += allnodes[inode.label-1:inode.label]
    #
    for i in range(len(EABnds1)):
        setname1 = 'Edge-AB-' + str(i+1+len(EABnds))
        setname2 = 'Edge-CD-' + str(i+1+len(ECDnds))
        a = mdb.models['Model-1'].rootAssembly
        a.Set(nodes=(EABnds1[i:i+1], ), name=setname1)
        #
        for j in range(len(ECDnds1)):
            dist = EABnds[i].coordinates[0] - ECDnds[j].coordinates[0]
            if abs(dist) < 1.0E-4:
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=(ECDnds1[j:j+1], ), name=setname2)
    #
    for i in range(len(EBCnds1)):
        setname1 = 'Edge-BC-' + str(i+1+len(EBCnds))
        setname2 = 'Edge-DA-' + str(i+1+len(EDAnds))
        a = mdb.models['Model-1'].rootAssembly
        a.Set(nodes=(EBCnds1[i:i+1], ), name=setname1)
        #
        for j in range(len(EDAnds1)):
            dist = EBCnds[i].coordinates[1] - EDAnds[j].coordinates[1]
            if abs(dist) < 1.0E-4:
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=(EDAnds1[j:j+1], ), name=setname2)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    allnodes = a.instances['Part-1-1'].nodes
    Vertnd1, Vertnd2, Vertnd3, Vertnd4 = allnodes[0:0], allnodes[0:0], allnodes[0:0], allnodes[0:0]
    #
    for i in range(2):
        instname = 'Part-'+str(i+1)+'-1'
        a = mdb.models['Model-1'].rootAssembly
        allnodes = a.instances[instname].nodes
        #
        for inode in allnodes:
            pt = inode.coordinates
            #
            if abs(pt[0]-rs[1]) < 1.0E-3 and abs(pt[1]-rs[3]) < 1.0E-3:
                Vertnd1 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[0]) < 1.0E-3 and abs(pt[1]-rs[3]) < 1.0E-3:
                Vertnd2 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[0]) < 1.0E-3 and abs(pt[1]-rs[2]) < 1.0E-3:
                Vertnd3 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[1]) < 1.0E-3 and abs(pt[1]-rs[2]) < 1.0E-3:
                Vertnd4 += allnodes[inode.label-1:inode.label]
    #
    for i in range(4):
        if i == 0:
            node = (Vertnd1[0:1],)
        if i == 1:
            node = (Vertnd2[0:1],)
        if i == 2:
            node = (Vertnd3[0:1],)
        if i == 3:
            node = (Vertnd4[0:1],)
        #
        a = mdb.models['Model-1'].rootAssembly
        a.Set(nodes=node, name='Vert-'+str(i+1))
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    a.ReferencePoint(point=(rs[0]*1.05, (rs[2]+rs[3])/2.0, 0.0))
    iD = a.features['RP-1'].id
    a.Set(referencePoints=(a.referencePoints[iD], ), name='Set-RP-1')
    #
    a = mdb.models['Model-1'].rootAssembly
    a.ReferencePoint(point=((rs[0]+rs[1])/2.0, rs[2]*1.05, 0.0))
    iD = a.features['RP-2'].id
    a.Set(referencePoints=(a.referencePoints[iD], ), name='Set-RP-2')
    #
    if len(EABnds) == len(ECDnds) and len(EABnds1) == len(ECDnds1):
        for i in range(max(len(EABnds)+len(EABnds1),len(ECDnds)+len(ECDnds1))):
            setname1, setname2 = 'Edge-CD-'+str(i+1), 'Edge-AB-'+str(i+1)
            xconst = 'EdgeEqs-AB-CD-X-'+str(i+1)
            yconst = 'EdgeEqs-AB-CD-Y-'+str(i+1)
            mdb.models['Model-1'].Equation(name=xconst, terms=((1.0, setname1, 1), (-1.0, setname2, 1), 
                (-1.0, 'Set-RP-2', 1)))
            mdb.models['Model-1'].Equation(name=yconst, terms=((1.0, setname1, 2), (-1.0, setname2, 2), 
                (-1.0, 'Set-RP-2', 2))) 
    #
    if len(EBCnds) == len(EDAnds) and len(EBCnds1) == len(EDAnds1):
        for i in range(max(len(EBCnds)+len(EBCnds1),len(EDAnds)+len(EDAnds1))):
            setname1, setname2 = 'Edge-BC-'+str(i+1), 'Edge-DA-'+str(i+1)
            xconst='EdgeEqs-BC-DA-X-'+str(i+1)
            yconst='EdgeEqs-BC-DA-Y-'+str(i+1)
            mdb.models['Model-1'].Equation(name=xconst, terms=((1.0, setname1, 1), (-1.0, setname2, 1), 
                (-1.0, 'Set-RP-1', 1)))
            mdb.models['Model-1'].Equation(name=yconst, terms=((1.0, setname1, 2), (-1.0, setname2, 2), 
                (-1.0, 'Set-RP-1', 2)))
    #
    mdb.models['Model-1'].Equation(name='VertEqs-X-1', terms=((1.0, 'Vert-2', 1), (-1.0, 'Vert-1', 1),
        (-1.0, 'Set-RP-1', 1)))
    mdb.models['Model-1'].Equation(name='VertEqs-Y-1', terms=((1.0, 'Vert-2', 2), (-1.0, 'Vert-1', 2), 
        (-1.0, 'Set-RP-1', 2)))
    #
    mdb.models['Model-1'].Equation(name='VertEqs-X-2', terms=((1.0, 'Vert-3', 1), (-1.0, 'Vert-4', 1), 
        (-1.0, 'Set-RP-1', 1)))
    mdb.models['Model-1'].Equation(name='VertEqs-Y-2', terms=((1.0, 'Vert-3', 2), (-1.0, 'Vert-4', 2),
        (-1.0, 'Set-RP-1', 2)))
    #                        
    mdb.models['Model-1'].Equation(name='VertEqs-X-3', terms=((1.0, 'Vert-4', 1), (-1.0, 'Vert-1', 1), 
        (-1.0, 'Set-RP-2', 1)))
    mdb.models['Model-1'].Equation(name='VertEqs-Y-3', terms=((1.0, 'Vert-4', 2), (-1.0, 'Vert-1', 2), 
        (-1.0, 'Set-RP-2', 2)))
    #
    #-------------------------------------------------------------------------------------
    # 
    a = mdb.models['Model-1'].rootAssembly
    region1, region2, region3 = a.sets['Set-RP-1'], a.sets['Set-RP-2'], a.sets['Vert-1']
    #
    mdb.models['Model-1'].DisplacementBC(name='BC-0', createStepName='Initial', region=region3, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
        ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    #
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', region=region1, u1=disp[0], u2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)   
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', region=region2, u1=0.0, u2=UNSET, ur3=0.0,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    #    
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-2', region=region1, u1=UNSET, u2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)   
    mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Step-2', region=region2, u1=0.0, u2=disp[1], ur3=0.0,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    #    
    mdb.models['Model-1'].DisplacementBC(name='BC-5', createStepName='Step-3', region=region1, u1=0.0, u2=disp[0]/2.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)   
    mdb.models['Model-1'].DisplacementBC(name='BC-6', createStepName='Step-3', region=region2, u1=disp[1]/2.0, u2=0.0, ur3=0.0,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    #
    #-------------------------------------------------------------------------------------
    #
    mdb.Job(name=jobname, model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, 
        echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, 
        multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
    mdb.jobs[jobname].writeInput(consistencyChecking=OFF)
    #
    mdb.saveAs(pathName=pathname)
    #
    mdb.jobs[jobname].submit(consistencyChecking=OFF)
    mdb.jobs[jobname].waitForCompletion()