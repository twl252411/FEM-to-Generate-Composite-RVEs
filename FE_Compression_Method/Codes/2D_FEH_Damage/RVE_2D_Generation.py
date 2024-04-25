#
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import string
import random
#
from GeometryShape2D import *
#
executeOnCaeStartup()
Mdb()
#
#------------------------------------------------------------------------------------
#
Inctypes = ['Circle', 'Lobular2', 'Lobular3', 'Lobular4', 'Spolygon3', 'Spolygon4', 'Ellipse', 'Kidney', 'Star']
RLength, Shdisp, Ampf, Filnum, IncId = 200.0, 0.0, 1.0, 1, 1
RLength1, PartName, IncType = RLength+2*Shdisp, 'Part-1', Inctypes[IncId-1]
#
UserVariables = {}
UserVariables.update({'Type':'DEFORMABLE_BODY'})
#
for ifil in [4]:
    #
    Mdb()
    #
    IncId = ifil + 1
    f1 = 'C:\\Temp\\Generated_Points_Angles\\'+Inctypes[ifil]+'\\NewCentroids'+str(5)+'.txt'
    f2 = 'C:\\Temp\\Generated_Points_Angles\\'+Inctypes[ifil]+'\\NewOriangles'+str(5)+'.txt'
    #
    Pathname = 'RVE_' + str(ifil+1) + '.cae'
    #
    #-----------------------------------------Circles------------------------------------------
    #
    if IncId == 1:
        IncSize = 6.0
        UserVariables.update({'Radius':IncSize*Ampf}) 
        ILength = UserVariables['Radius']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Circles(PartName)
    #
    #-----------------------------------------Lobular2------------------------------------------
    #
    elif IncId == 2:
        IncSize = 4.2
        UserVariables.update({'Radius':IncSize*Ampf}) 
        ILength = 2.0*UserVariables['Radius']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Lobular2s(PartName)
    #
    #-----------------------------------------Lobular3------------------------------------------
    #
    elif IncId == 3:
        IncSize = 3.4
        UserVariables.update({'Radius':IncSize*Ampf}) 
        ILength = (2.0/sqrt(3)+1.0)*UserVariables['Radius']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Lobular3s(PartName)
    #
    #-----------------------------------------Lobular4------------------------------------------
    #
    elif IncId == 4:
        IncSize = 2.85
        UserVariables.update({'Radius':IncSize*Ampf}) 
        ILength = (1+sqrt(2))*UserVariables['Radius']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Lobular4s(PartName)
    #
    #-----------------------------------------Spolygon3-----------------------------------------
    #
    elif IncId == 5:
        IncSize = [17.0, 2.25]
        UserVariables.update({'Slength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
        ILength = sqrt(3)/3.0*UserVariables['Slength']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Spolygon3s(PartName)
    #
    #-----------------------------------------Spolygon4-----------------------------------------
    #
    elif IncId == 6:
        IncSize = [11.0, 2.75]
        UserVariables.update({'Slength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
        ILength = sqrt(2)/2.0*UserVariables['Slength']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Spolygon4s(PartName)
    #
    #------------------------------------------Ellipses------------------------------------------
    #
    elif IncId == 7:
        IncSize = 8.5
        UserVariables.update({'Axis1':IncSize*Ampf, 'Axis2':IncSize/2.0*Ampf}) 
        ILength = UserVariables['Axis1']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Ellipses(PartName)
    #
    #-------------------------------------------Kidneys-------------------------------------------
    #
    elif IncId == 8:
        IncSize = [5.6, 8.3, 3.8, 5.8]
        UserVariables.update({'R1':IncSize[0]*Ampf, 'R2':IncSize[1]*Ampf, 'K1':IncSize[2]*Ampf, 'a':IncSize[3]*Ampf}) 
        ILength = UserVariables['R2']
        Object = GeometryShape2D(UserVariables)
        sp = Object.Kidneys(PartName)
    #
    #-------------------------------Five-stars----------------------------------
    #
    else:
        IncSize = [8.6, 2.2]
        UserVariables.update({'Alength':IncSize[0]*Ampf, 'Radius':IncSize[1]*Ampf}) 
        ILength = UserVariables['Alength']*(cos(18.0/180*pi) + sin(18.0/180*pi)*tan(54.0/180*pi))
        Object = GeometryShape2D(UserVariables)
        sp = Object.F5stars(PartName)
    #
    #------------------------------------------------------------------------------------
    #
    p = mdb.models['Model-1'].parts['Part-1']
    dic = p.getMassProperties( )
    V1 = dic['area']
    #
    #------------------------------------------------------------------------------------
    #
    myfile = open(f1,'r')
    lines = myfile.readlines()
    TranVec = []
    for line in lines:
        ele = string.split(line,',')
        TranVec.append((float(ele[0]),float(ele[1])))
    #
    myfile = open(f2,'r')
    lines = myfile.readlines()
    RoAngle = []
    for line in lines:
        ele = string.split(line,',')
        RoAngle.append((float(ele[0])))
    #
    #------------------------------------------------------------------------------------
    #
    instanceList = ()
    for inc in range(len(TranVec)):
        a = mdb.models['Model-1'].rootAssembly
        p = mdb.models['Model-1'].parts['Part-1']
        InsName = 'Part-1-' + str(inc+1)
        a.Instance(name=InsName, part=p, dependent=OFF)
        a.rotate(instanceList=(InsName, ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(0.0, 0.0, 1.0), angle=RoAngle[inc])
        a.translate(instanceList=(InsName, ), vector=(TranVec[inc][0], TranVec[inc][1], 0.0))	
        a.translate(instanceList=(InsName, ), vector=(RLength/2.0, RLength/2.0, 0.0))	
        instanceList = instanceList + ((a.instances[InsName], ))
    #
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanMerge(name='Part-2', instances=instanceList, originalInstances=DELETE, domain=GEOMETRY)   
    del a.instances['Part-2-1'] 
    del mdb.models['Model-1'].parts['Part-1']
    mdb.models['Model-1'].parts.changeKey(fromName='Part-2', toName='Part-1')
    #
    p = mdb.models['Model-1'].parts['Part-1']
    dic = p.getMassProperties( )
    V2 = dic['area']
    #
    InSecFlag = abs(len(TranVec)*V1 - V2)/V1
    #
    a = mdb.models['Model-1'].rootAssembly
    p1 = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p1, dependent=OFF)
    a.Instance(name='Part-1-2', part=p1, dependent=OFF)
    #
    #------------------------------------------------------------------------------------
    #
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(RLength, RLength))
    p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-2']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    #
    a = mdb.models['Model-1'].rootAssembly
    p1 = mdb.models['Model-1'].parts['Part-2']
    a.Instance(name='Part-2-1', part=p1, dependent=OFF)
    #
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='Part-3',
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-1-2'], 
        cuttingInstances=(a.instances['Part-2-1'], ), originalInstances=DELETE)
    a.InstanceFromBooleanCut(name='Part-4', 
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'],
        cuttingInstances=(a.instances['Part-3-1'], ), originalInstances=DELETE)
    #
    del mdb.models['Model-1'].parts['Part-1']
    del mdb.models['Model-1'].parts['Part-2']
    del mdb.models['Model-1'].parts['Part-3']
    a = mdb.models['Model-1'].rootAssembly
    a.deleteFeatures(('Part-4-1',))
    #
    mdb.models['Model-1'].parts.changeKey(fromName='Part-4', toName='Part-2')
    #
    #------------------------------------------------------------------------------------
    #
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(RLength1, RLength1))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseShell(sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    #		    
    a = mdb.models['Model-1'].rootAssembly
    p1 = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p1, dependent=OFF)
    #
    p1 = mdb.models['Model-1'].parts['Part-2']
    a.Instance(name='Part-2-1', part=p1, dependent=OFF)
    #a.translate(instanceList=('Part-2-1', ), vector=(Shdisp, Shdisp, 0.0))
    #
    a = mdb.models['Model-1'].rootAssembly
    a.InstanceFromBooleanCut(name='Part-3',
        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], 
        cuttingInstances=(a.instances['Part-2-1'], ), originalInstances=DELETE)
    #
    a = mdb.models['Model-1'].rootAssembly
    a.deleteFeatures(('Part-3-1',))
    del mdb.models['Model-1'].parts['Part-1']
    #
    mdb.models['Model-1'].parts.changeKey(fromName='Part-3', toName='Part-1')
    #
    a = mdb.models['Model-1'].rootAssembly
    p1 = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p1, dependent=ON)
    p1 = mdb.models['Model-1'].parts['Part-2']
    a.Instance(name='Part-2-1', part=p1, dependent=ON)  
    #a.translate(instanceList=('Part-2-1', ), vector=(Shdisp, Shdisp, 0.0))
    #
    #-------------------------------------------------------------------------------------------------------
    #
    dic = mdb.models['Model-1'].parts['Part-2'].getMassProperties( )
    volum2 = dic['area']
    dic = mdb.models['Model-1'].parts['Part-1'].getMassProperties( )
    volum1 = dic['area']
    #
    Fiberfraction=volum2/(volum2+volum1)
    print 'The volume fraction of fibers is'
    print Fiberfraction
    #
    #------------------------------------------------------------------------------------
    #
    mdb.saveAs(pathName=Pathname)