import random
import string
import numpy as np
from abaqus import *
from caeModules import *
from abaqusConstants import *
from driverUtils import executeOnCaeStartup
#
executeOnCaeStartup()
Mdb()
#
#-------------------------------------------------------------------------------------
#
session.journalOptions.setValues(replayGeometry=INDEX, recoverGeometry=INDEX)
#
for ifile in range(9):
    caename, pathname, jobname = 'RVE_'+str(ifile+1)+'.cae', 'FE_Model_'+str(ifile+1)+'.cae', 'Job-'+str(ifile+1)
    openMdb(pathName=caename)
    #
    rs = [200.0, 0.0, 200.0, 0.0]
    mshsize, disp = 0.75, (rs[0]-rs[1])*0.01
    #
    #-------------------------------------------------------------------------------------
    #
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].DruckerPrager(table=((29.0, 0.8, 29.0), ))
    mdb.models['Model-1'].materials['Material-1'].druckerPrager.DruckerPragerHardening(type=TENSION, table=((0.000121, 0.0), ))
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((0.0051, 0.35), ))
    mdb.models['Model-1'].materials['Material-1'].DuctileDamageInitiation(table=((0.25, -0.3333, 0.0), (0.025, 0.3333, 0.0), ))
    mdb.models['Model-1'].materials['Material-1'].ductileDamageInitiation.DamageEvolution(type=ENERGY, table=((1.0E-4, ), ))  
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    region = regionToolset.Region(faces=p.faces)
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, offsetType=MIDDLE_SURFACE, 
        offsetField='', thicknessAssignment=FROM_SECTION)
    #
    mdb.models['Model-1'].Material(name='Material-2')
    mdb.models['Model-1'].materials['Material-2'].Elastic(table=((0.013, 0.46), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='Material-2', thickness=None)
    p = mdb.models['Model-1'].parts['Part-2']
    region = regionToolset.Region(faces=p.faces)
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, offsetType=MIDDLE_SURFACE, 
        offsetField='', thicknessAssignment=FROM_SECTION)
    #
    mdb.models['Model-1'].Material(name='Material-3')
    mdb.models['Model-1'].materials['Material-3'].Elastic(type=TRACTION, table=((0.1, 0.1, 0.1), ))
    mdb.models['Model-1'].materials['Material-3'].MaxsDamageInitiation(table=((6.2E-5, 8.4E-5, 8.4E-5), ))
    mdb.models['Model-1'].materials['Material-3'].maxsDamageInitiation.DamageEvolution(type=ENERGY, mixedModeBehavior=BK, 
        power=1.2, table=((2.0E-5, 1.0E-4, 1.0E-4), ))
    mdb.models['Model-1'].materials['Material-3'].maxsDamageInitiation.DamageStabilizationCohesive(cohesiveCoeff=0.0001)
    mdb.models['Model-1'].CohesiveSection(name='Section-3', material='Material-3', response=TRACTION_SEPARATION, outOfPlaneThickness=None)
    #
    #-------------------------------------------------------------------------------------
    #
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', maxNumInc=100000, initialInc=0.001, minInc=1e-20, maxInc=0.02)
    mdb.models['Model-1'].steps['Step-1'].setValues(nlgeom=ON)
    mdb.models['Model-1'].steps['Step-1'].control.setValues(allowPropagation=OFF, resetDefaultValues=OFF,
        timeIncrementation=(4.0, 40.0, 9.0, 16.0, 10.0, 4.0, 12.0, 20.0, 6.0, 3.0, 50.0)) 
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'PE', 'PEEQ', 'LE', 'U', 'RF', 'CF', 
        'CSTRESS', 'CDISP', 'DAMAGEC', 'DAMAGET', 'SDEG', 'DMICRT', 'EVOL', 'IVOL', 'STATUS'))
    #
    #-------------------------------------------------------------------------------------
    #
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=mshsize, deviationFactor=0.1, minSizeFactor=0.1)
    #
    p = mdb.models['Model-1'].parts['Part-1']
    p.setMeshControls(regions=p.faces, elemShape=QUAD_DOMINATED)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, hourglassControl=ENHANCED, 
        distortionControl=DEFAULT, elemDeletion=ON, maxDegradation=0.8)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    p.setElementType(regions=(p.faces, ), elemTypes=(elemType1, elemType2))
    p.generateMesh()
    #
    p = mdb.models['Model-1'].parts['Part-2']
    p.seedPart(size=mshsize, deviationFactor=0.1, minSizeFactor=0.1)
    #
    p = mdb.models['Model-1'].parts['Part-2']
    p.setMeshControls(regions=p.faces, elemShape=QUAD_DOMINATED)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    p.setElementType(regions=(p.faces, ), elemTypes=(elemType1, elemType2))
    p.generateMesh()
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-1-1'].edges
    selectedges = alledges[0:0]
    #
    for iedge in alledges:
        pt = iedge.pointOn[0]
        if abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
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
        if abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            selectedges += alledges[iedge.index:iedge.index+1]
    #
    a = mdb.models['Model-1'].rootAssembly
    a.Surface(side1Edges=selectedges, name='Slave-1')
    #
    #-------------------------------------------------------------------------------------
    #
    p = mdb.models['Model-1'].parts['Part-1']
    cohedges = p.edges[0:0]
    for iedge in p.edges:
        pt = iedge.pointOn[0]
        if abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            cohedges += p.edges[iedge.index:iedge.index+1]
    p.Set(edges=cohedges, name='Cohedges')
    #
    p = mdb.models['Model-1'].parts['Part-1']
    tnumele, tnumnod = len(p.elements), len(p.nodes)
    pickedEdges = regionToolset.Region(side1Edges=p.sets['Cohedges'].edges)
    p.insertElements(edges=pickedEdges)
    #
    p = mdb.models['Model-1'].parts['Part-1']
    t1numele, t1numnod = len(p.elements), len(p.nodes)
    feles = p.elements[tnumele:t1numele]
    p.Set(elements=feles, name='Cohesive-Elements')
    p.Surface(face3Elements=feles, name='Cohesive-TopSurf')
    p.Surface(face1Elements=feles, name='Cohesive-BottomSurf')
    #
    p = mdb.models['Model-1'].parts['Part-1']
    nodes = p.nodes[tnumnod:t1numnod] 
    p.Set(nodes=nodes, name='Cohesive-TopNodes')
    nodes = p.sets['Cohedges'].nodes
    p.Set(nodes=nodes, name='Cohesive-BottomNodes')
    #
    elemType1 = mesh.ElemType(elemCode=COH2D4, elemLibrary=STANDARD, elemDeletion=ON, viscosity=0.001, maxDegradation=0.95)
    p = mdb.models['Model-1'].parts['Part-1']
    pickedRegions = p.sets['Cohesive-Elements']
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    #
    p = mdb.models['Model-1'].parts['Part-1']
    region = p.sets['Cohesive-Elements']
    p.SectionAssignment(region=region, sectionName='Section-3', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    #
    a = mdb.models['Model-1'].rootAssembly
    region1, region2 = a.instances['Part-1-1'].surfaces['Cohesive-TopSurf'], a.surfaces['Slave-1']
    mdb.models['Model-1'].Tie(name='Tie-1', master=region2, slave=region1, positionToleranceMethod=COMPUTED, adjust=OFF, 
        tieRotations=OFF, thickness=ON)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    alledges = a.instances['Part-1-1'].edges
    selectedges1 = alledges[0:0]
    selectedges2 = alledges[0:0]
    #
    for iins in range(2):
        alledges = a.instances['Part-'+str(iins+1)+'-1'].edges
        for iedge in alledges:
            pt = iedge.pointOn[0]
            if abs(pt[0]-rs[1]) < 1.0E-4:
                selectedges1 += alledges[iedge.index:iedge.index+1]
            if abs(pt[1]-rs[3]) < 1.0E-4:
                selectedges2 += alledges[iedge.index:iedge.index+1]
    #
    a = mdb.models['Model-1'].rootAssembly
    a.Set(edges=selectedges1, name='Fixed-Edges-X')
    a.Set(edges=selectedges2, name='Fixed-Edges-Y')
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, constraints=ON, connectors=ON, 
        engineeringFeatures=ON, optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF, mesh=ON)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    allnodes = a.instances['Part-1-1'].nodes
    setnds = a.sets['Common-Surf-1'].nodes
    selcnds = setnds[0:0]
    for isetn in setnds:
        pt = isetn.coordinates
        if abs(pt[0]-rs[0]) < 1.0E-4 or abs(pt[0]-rs[1]) < 1.0E-4 or abs(pt[1]-rs[2]) < 1.0E-4 or abs(pt[1]-rs[3]) < 1.0E-4:
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
        if abs(pt[1]-rs[3]) < 1.0E-4 and abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4:
            if inode not in selcnds:
                EABnds += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[0]) < 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            if inode not in selcnds:
                EBCnds += allnodes[inode.label-1:inode.label]
        if abs(pt[1]-rs[2]) < 1.0E-4 and abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4:
            if inode not in selcnds:
                ECDnds += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[1]) < 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            if inode not in selcnds:
                EDAnds += allnodes[inode.label-1:inode.label]
    #
    TmpCoords = []
    for i in range(len(EABnds)):
        TmpCoords += [EABnds[i].coordinates[0]]
    for i in range(0,len(EABnds)):
        for j in range(len(EABnds)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(EABnds)):
        for j in range(0,len(EABnds)):
            if abs(TmpCoords[i]-EABnds[j].coordinates[0]) < 1.0E-6:
                node = (allnodes[EABnds[j].label-1:EABnds[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-AB-' + str(i+1))
    #
    TmpCoords = []
    for i in range(len(ECDnds)):
        TmpCoords += [ECDnds[i].coordinates[0]]
    for i in range(0,len(ECDnds)):
        for j in range(len(ECDnds)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(ECDnds)):
        for j in range(0,len(ECDnds)):
            if abs(TmpCoords[i]-ECDnds[j].coordinates[0]) < 1.0E-6:
                node = (allnodes[ECDnds[j].label-1:ECDnds[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-CD-' + str(i+1))
    #
    TmpCoords = []
    for i in range(len(EBCnds)):
        TmpCoords += [EBCnds[i].coordinates[1]]
    for i in range(0,len(EBCnds)):
        for j in range(len(EBCnds)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(EBCnds)):
        for j in range(0,len(EBCnds)):
            if abs(TmpCoords[i]-EBCnds[j].coordinates[1]) < 1.0E-6:
                node = (allnodes[EBCnds[j].label-1:EBCnds[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-BC-' + str(i+1))
    #
    TmpCoords = []
    for i in range(len(EDAnds)):
        TmpCoords += [EDAnds[i].coordinates[1]]
    for i in range(0,len(EDAnds)):
        for j in range(len(EDAnds)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(EDAnds)):
        for j in range(0,len(EDAnds)):
            if abs(TmpCoords[i]-EDAnds[j].coordinates[1]) < 1.0E-6:
                node = (allnodes[EDAnds[j].label-1:EDAnds[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-DA-' + str(i+1))
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
        if abs(pt[1]-rs[3]) < 1.0E-4 and abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4:
            EABnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[0]) < 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            EBCnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[1]-rs[2]) < 1.0E-4 and abs(pt[0]-rs[0]) > 1.0E-4 and abs(pt[0]-rs[1]) > 1.0E-4:
            ECDnds1 += allnodes[inode.label-1:inode.label]
        if abs(pt[0]-rs[1]) < 1.0E-4 and abs(pt[1]-rs[2]) > 1.0E-4 and abs(pt[1]-rs[3]) > 1.0E-4:
            EDAnds1 += allnodes[inode.label-1:inode.label]
    #
    TmpCoords = []
    for i in range(len(EABnds1)):
        TmpCoords += [EABnds1[i].coordinates[0]]
    for i in range(0,len(EABnds1)):
        for j in range(len(EABnds1)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp	
    for i in range(0,len(EABnds1)):
        for j in range(0,len(EABnds1)):
            if abs(TmpCoords[i]-EABnds1[j].coordinates[0]) < 1.0E-6:
                node = (allnodes[EABnds1[j].label-1:EABnds1[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-AB-' + str(i+1+len(EABnds)))
    #
    TmpCoords = []
    for i in range(len(ECDnds1)):
        TmpCoords += [ECDnds1[i].coordinates[0]]
    for i in range(0,len(ECDnds1)):
        for j in range(len(ECDnds1)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp	
    for i in range(0,len(ECDnds1)):
        for j in range(0,len(ECDnds1)):
            if abs(TmpCoords[i]-ECDnds1[j].coordinates[0]) < 1.0E-6:
                node = (allnodes[ECDnds1[j].label-1:ECDnds1[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-CD-' + str(i+1+len(ECDnds)))
    #
    TmpCoords = []
    for i in range(len(EBCnds1)):
        TmpCoords += [EBCnds1[i].coordinates[1]]
    for i in range(0,len(EBCnds1)):
        for j in range(len(EBCnds1)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(EBCnds1)):
        for j in range(0,len(EBCnds1)):
            if abs(TmpCoords[i]-EBCnds1[j].coordinates[1]) < 1.0E-6:
                node = (allnodes[EBCnds1[j].label-1:EBCnds1[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-BC-' + str(i+1+len(EBCnds)))
    #
    TmpCoords = []
    for i in range(len(EDAnds1)):
        TmpCoords += [EDAnds1[i].coordinates[1]]
    for i in range(0,len(EDAnds1)):
        for j in range(len(EDAnds1)-1,i,-1):
            if TmpCoords[j] < TmpCoords[j-1]:
                Temp = TmpCoords[j-1]
                TmpCoords[j-1] = TmpCoords[j]
                TmpCoords[j] = Temp
    for i in range(0,len(EDAnds1)):
        for j in range(0,len(EDAnds1)):
            if abs(TmpCoords[i]-EDAnds1[j].coordinates[1]) < 1.0E-6:
                node = (allnodes[EDAnds1[j].label-1:EDAnds1[j].label], )
                a = mdb.models['Model-1'].rootAssembly
                a.Set(nodes=node, name='Edge-DA-' + str(i+1+len(EDAnds)))
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
            if abs(pt[0]-rs[1]) < 1.0E-4 and abs(pt[1]-rs[3]) < 1.0E-4:
                Vertnd1 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[0]) < 1.0E-4 and abs(pt[1]-rs[3]) < 1.0E-4:
                Vertnd2 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[0]) < 1.0E-4 and abs(pt[1]-rs[2]) < 1.0E-4:
                Vertnd3 += allnodes[inode.label-1:inode.label]
            if abs(pt[0]-rs[1]) < 1.0E-4 and abs(pt[1]-rs[2]) < 1.0E-4:
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
        for i in range(len(EABnds)+len(EABnds1)):
            setname1, setname2 = 'Edge-AB-'+str(i+1), 'Edge-CD-'+str(i+1)
            xconst = 'EdgeEqs-AB-CD-X-'+str(i+1)
            yconst = 'EdgeEqs-AB-CD-Y-'+str(i+1)
            mdb.models['Model-1'].Equation(name=xconst, terms=((1.0, setname1, 1), (-1.0, setname2, 1), 
                (-1.0, 'Set-RP-2', 1)))
            mdb.models['Model-1'].Equation(name=yconst, terms=((1.0, setname1, 2), (-1.0, setname2, 2), 
                (-1.0, 'Set-RP-2', 2))) 
    #
    if len(EBCnds) == len(EDAnds) and len(EBCnds1) == len(EDAnds1):
        for i in range(len(EBCnds)+len(EBCnds1)):
            setname1, setname2 = 'Edge-BC-'+str(i+1), 'Edge-DA-'+str(i+1)
            xconst='EdgeEqs-BC-DA-X-'+str(i+1)
            yconst='EdgeEqs-BC-DA-Y-'+str(i+1)
            mdb.models['Model-1'].Equation(name=xconst, terms=((1.0, setname1, 1), (-1.0, setname2, 1), 
                (-1.0, 'Set-RP-1', 1)))
            mdb.models['Model-1'].Equation(name=yconst, terms=((1.0, setname1, 2), (-1.0, setname2, 2), 
                (-1.0, 'Set-RP-1', 2)))
    #
    #mdb.models['Model-1'].Equation(name='VertEqs-X-1', terms=((1.0, 'Vert-2', 1), (-1.0, 'Vert-1', 1),
    #    (-1.0, 'Set-RP-1', 1)))
    mdb.models['Model-1'].Equation(name='VertEqs-Y-1', terms=((1.0, 'Vert-2', 2), (-1.0, 'Vert-1', 2), 
        (-1.0, 'Set-RP-1', 2)))
    #
    #mdb.models['Model-1'].Equation(name='VertEqs-X-2', terms=((1.0, 'Vert-3', 1), (-1.0, 'Vert-4', 1), 
    #    (-1.0, 'Set-RP-1', 1)))
    mdb.models['Model-1'].Equation(name='VertEqs-Y-2', terms=((1.0, 'Vert-3', 2), (-1.0, 'Vert-4', 2),
        (-1.0, 'Set-RP-1', 2)))
    #                        
    mdb.models['Model-1'].Equation(name='VertEqs-X-3', terms=((1.0, 'Vert-4', 1), (-1.0, 'Vert-1', 1), 
        (-1.0, 'Set-RP-2', 1)))
    #mdb.models['Model-1'].Equation(name='VertEqs-Y-3', terms=((1.0, 'Vert-4', 2), (-1.0, 'Vert-1', 2), 
    #    (-1.0, 'Set-RP-2', 2)))
    #
    #-------------------------------------------------------------------------------------
    # 
    a = mdb.models['Model-1'].rootAssembly
    region1, region2 = a.sets['Set-RP-1'], a.sets['Set-RP-2']
    region3, region4 = a.sets['Fixed-Edges-X'], a.sets['Fixed-Edges-Y']
    #
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', region=region1, u1=disp, u2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', region=region2, u1=0.0, u2=UNSET, ur3=0.0,
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', region=region3, u1=0.0, u2=UNSET, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Step-1', region=region4, u1=UNSET, u2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
    #
    #-------------------------------------------------------------------------------------
    #
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['Set-RP-1']
    mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-1', createStepName='Step-1', variables=('U1', 'RF1'), 
        region=region, sectionPoints=DEFAULT, rebar=EXCLUDE)
    #
    mdb.Job(name=jobname, model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, 
        echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, 
        multiprocessingMode=DEFAULT, parallelizationMethodExplicit=DOMAIN, numDomains=16, activateLoadBalancing=False, numCpus=16, 
        numGPUs=0)
    mdb.jobs[jobname].writeInput(consistencyChecking=OFF)
    #
    mdb.saveAs(pathName=pathname)
    #
    #mdb.jobs[jobname].submit(consistencyChecking=OFF)
    #mdb.jobs[jobname].waitForCompletion()