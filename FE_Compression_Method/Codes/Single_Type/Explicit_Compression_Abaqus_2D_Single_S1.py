#
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import string
import random
import time
#
from GeometryShape2D import *
from GetXYCoordinates import *
#
executeOnCaeStartup()
Mdb()
#
#------------------------------------------------------------------------------------
#
session.journalOptions.setValues(replayGeometry=INDEX, recoverGeometry=INDEX)
#
PartName, Pathname, JobName, IncId = 'Part-1', 'Test-1.cae', 'Job-1', 6
RLength, Meshsize, Ampf, Inialf, Finalf = 200.0, 0.25, 1.05, 4.0/4.0, 2.0/4.0
#
UserVariables = {}
UserVariables.update({'Type':'DISCRETE_RIGID_SURFACE', 'dPid':2})  #'DEFORMABLE_BODY' #  
#
#-----------------------------------------Circles------------------------------------------
#
if IncId == 1:
    IncSize = 6.0
    UserVariables.update({'Radius':IncSize*Ampf}) 
    ILength = UserVariables['Radius']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Circles(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-----------------------------------------Lobular2------------------------------------------
#
elif IncId == 2:
    IncSize = 4.2
    UserVariables.update({'Radius':IncSize*Ampf}) 
    ILength = 2.0*UserVariables['Radius']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Lobular2s(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-----------------------------------------Lobular3------------------------------------------
#
elif IncId == 3:
    IncSize = 3.4
    UserVariables.update({'Radius':IncSize*Ampf}) 
    ILength = (2.0/sqrt(3)+1.0)*UserVariables['Radius']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Lobular3s(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-----------------------------------------Lobular4------------------------------------------
#
elif IncId == 4:
    IncSize = 2.85
    UserVariables.update({'Radius':IncSize*Ampf}) 
    ILength = (1+sqrt(2))*UserVariables['Radius']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Lobular4s(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-----------------------------------------Spolygon3-----------------------------------------
#
elif IncId == 5:
    IncSize = [17.0, 2.25]
    UserVariables.update({'Slength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
    ILength = sqrt(3)/3.0*UserVariables['Slength']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Spolygon3s(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-----------------------------------------Spolygon4-----------------------------------------
#
elif IncId == 6:
    IncSize = [11.5, 2.75]
    UserVariables.update({'Slength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
    ILength = sqrt(2)/2.0*UserVariables['Slength']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Spolygon4s(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#------------------------------------------Ellipses------------------------------------------
#
elif IncId == 7:
    IncSize = 8.5
    UserVariables.update({'Axis1':IncSize*Ampf, 'Axis2':IncSize/2.0*Ampf}) 
    ILength = UserVariables['Axis1']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Ellipses(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-------------------------------------------Kidneys-------------------------------------------
#
elif IncId == 8:
    IncSize = [5.6, 8.3, 3.8, 5.8]
    UserVariables.update({'R1':IncSize[0]*Ampf, 'R2':IncSize[1]*Ampf, 'K1':IncSize[2]*Ampf, 'a':IncSize[3]*Ampf}) 
    ILength = UserVariables['R2']
    Object = GeometryShape2D(UserVariables)
    sp = Object.Kidneys(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#-------------------------------Five-stars----------------------------------
#
else:
    IncSize = [8.6, 2.2]
    UserVariables.update({'Alength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
    ILength = UserVariables['Alength']*(cos(18.0/180*pi) + sin(18.0/180*pi)*tan(54.0/180*pi))
    Object = GeometryShape2D(UserVariables)
    sp = Object.F5stars(PartName)
    pa = GetXYCoordinates(UserVariables).Partition(PartName)
    Coord1 = GetXYCoordinates(UserVariables).GetCoords(PartName)
#
#------------------------------------------------------------------------------------
#
p = mdb.models['Model-1'].parts[PartName]
p.ReferencePoint(point=(0.0, 0.0, 0.0))
refp = p.features['RP']
pid1 = refp.id
#
#------------------------------------------------------------------------------------
#
filename = 'Midpoints.txt'
myfile = open(filename,'r')
lines = myfile.readlines()
TranVec = []
for iline in lines:
    ele = string.split(iline,',')
    TranVec.append((float(ele[0]),float(ele[1])))	
myfile.close()
#
filename = 'Oriangles.txt'
myfile = open(filename,'r')
lines = myfile.readlines()
RoAngle = []
for iline in lines:
    ele = string.split(iline,',')
    RoAngle.append((float(ele[0])))
myfile.close()
#
#------------------------------------------------------------------------------------
#
for inc in range(len(TranVec)):
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts[PartName]
    InsName = 'Part-1-' + str(inc+1)
    a.Instance(name=InsName, part=p, dependent=OFF)
    #
    r1 = a.instances[InsName].referencePoints
    refPoints = (r1[pid1], )
    Setname = 'Set-P-' + str(inc+1)
    a.Set(referencePoints=refPoints, name=Setname)
    #
    partInstances =(a.instances[InsName], )
    a.seedPartInstance(regions=partInstances, size=Meshsize, deviationFactor=0.1, minSizeFactor=0.1)
    a.generateMesh(regions=partInstances)
    #
    Insnodes = a.instances[InsName].nodes
    for inode in Insnodes:
        x,y,z = inode.coordinates       
        if abs(x-Coord1) < 1.0e-4 and abs(y) < 1.0e-4:
            Setname = 'Set-' + str(inc+1) + '-1'
            node1 = (Insnodes[inode.label-1:inode.label], )
            a = mdb.models['Model-1'].rootAssembly
            a.Set(nodes=node1, name=Setname)
    #
    a.rotate(instanceList=(InsName, ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 0.0, 1.0), angle=RoAngle[inc])
    a.translate(instanceList=(InsName, ), vector=(TranVec[inc][0], TranVec[inc][1], 0.0))	
#
#-------------------------------------------------------------------------------------------------------
#
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.Line(point1=(-Inialf*RLength, 0.0), point2=(Inialf*RLength, 0.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=TWO_D_PLANAR, type=ANALYTIC_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['Part-2']
p.AnalyticRigidSurf2DPlanar(sketch=s)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
#
p = mdb.models['Model-1'].parts['Part-2']
v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[0], rule=MIDDLE))
refp = p.features['RP']
pid2 = refp.id
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-2']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
a.translate(instanceList=('Part-2-1', ), vector=(0.0, Inialf*RLength, 0.0))
a.Instance(name='Part-2-2', part=p, dependent=OFF)
a.translate(instanceList=('Part-2-2', ), vector=(0.0, -Inialf*RLength, 0.0))
#
#-------------------------------------------------------------------------------------------------------
#
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(0.0, Inialf*RLength), point2=(0.0, -Inialf*RLength))
p = mdb.models['Model-1'].Part(name='Part-3', dimensionality=TWO_D_PLANAR, type=ANALYTIC_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['Part-3']
p.AnalyticRigidSurf2DPlanar(sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
#
p = mdb.models['Model-1'].parts['Part-3']
v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=p.InterestingPoint(edge=e[0], rule=MIDDLE))
refp = p.features['RP']
pid3 = refp.id
#
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Part-3']
a.Instance(name='Part-3-1', part=p, dependent=OFF)
a.translate(instanceList=('Part-3-1', ), vector=(Inialf*RLength, 0.0, 0.0))
a.Instance(name='Part-3-2', part=p, dependent=OFF)
a.translate(instanceList=('Part-3-2', ), vector=(-Inialf*RLength, 0.0, 0.0))
#
#-------------------------------------------------------------------------------------------------------
#
alf = (Inialf - 0.5)/(Inialf - Finalf)
mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', timePeriod=25.0, timeIncrementationMethod=FIXED_USER_DEFINED_INC, 
    userDefinedInc=1.0E-4, improvedDtMethod=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=('U', 'COORD'))    
mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (10.0, 1.0), (15.0, 0.5), 
    (20.0, 1.0), (25.0, alf*1.0)))
#
#-------------------------------------------------------------------------------------------------------
#
p = mdb.models['Model-1'].parts[PartName]
r = p.referencePoints
region = (r[pid1], )
mdb.models['Model-1'].parts[PartName].engineeringFeatures.PointMassInertia(name='Inertia-1', region=region, 
    mass=1.0E-6, i11=1.0E-18, i22=1.0E-18, i33=1.0E-18, alpha=0.0, composite=0.0)
#
#-------------------------------------------------------------------------------------------------------
#
for i in range(len(TranVec)):
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-'+str(i+1)].edges
    side2Edges1 = s1[0:len(s1)]
    a.Surface(side2Edges=side2Edges1, name='Surf-1-'+str(i+1))
#
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-1'].edges
side2Edges1 = s1[0:1]
a.Surface(side2Edges=side2Edges1, name='Surf-2')
#
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-2-2'].edges
side1Edges1 = s1[0:1]
a.Surface(side1Edges=side1Edges1, name='Surf-3')
#
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-1'].edges
side2Edges1 = s1[0:1]
a.Surface(side2Edges=side2Edges1, name='Surf-4')
#
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-3-2'].edges
side1Edges1 = s1[0:1]
a.Surface(side1Edges=side1Edges1, name='Surf-5')
#
#-------------------------------------------------------------------------------------------------------
#
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(formulation=PENALTY, directionality=ISOTROPIC, 
    slipRateDependency=OFF, pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((0.001, ), ), 
    shearStressLimit=None, maximumElasticSlip=FRACTION, fraction=0.001, elasticSlipStiffness=None)
mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT)
#
mdb.models['Model-1'].ContactExp(name='Int-1', createStepName='Initial')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(stepName='Initial', 
    assignments=((GLOBAL, SELF, 'IntProp-1'), ))
#
#-------------------------------------------------------------------------------------------------------
#	
refPoints1 = ()
for inc in range(len(TranVec)): 
    a = mdb.models['Model-1'].rootAssembly
    InstName = 'Part-1-'+str(inc+1)
    r1 = a.instances[InstName].referencePoints
    refPoints1 = refPoints1 + (r1[pid1], )  
#			  
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-Ini', createStepName='Initial', region=region, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)  
#    
#---------------------------------------------
#      
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Part-2-1'].referencePoints
refPoints1=(r1[pid2], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', region=region, u1=0.0, u2=-(Inialf-Finalf)*RLength, ur3=0.0, 
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
#
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Part-2-2'].referencePoints
refPoints1=(r1[pid2], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', region=region, u1=0.0, u2=(Inialf-Finalf)*RLength, ur3=0.0, 
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
#
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Part-3-1'].referencePoints
refPoints1=(r1[pid3], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Step-1', region=region, u2=0.0, u1=-(Inialf-Finalf)*RLength, ur3=0.0, 
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
#
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['Part-3-2'].referencePoints
refPoints1=(r1[pid3], )
region = regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].DisplacementBC(name='BC-5', createStepName='Step-1', region=region, u2=0.0, u1=(Inialf-Finalf)*RLength, ur3=0.0,
    amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)  
#
#-------------------------------------------------------------------------------------------------------
#    
mdb.Job(name=JobName, model='Model-1', description='', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=DOUBLE, nodalOutputPrecision=FULL, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, 
    historyPrint=OFF, userSubroutine='', scratch='', resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=64, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=64)
mdb.jobs[JobName].writeInput(consistencyChecking=OFF)
#
#-------------------------------------------------------------------------------------------------------
#
mdb.saveAs(pathName=Pathname)