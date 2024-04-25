from abaqus import *
from abaqusConstants import *
import os
import job
from odbAccess import *	
import string
import numpy as np
#
#-------------------------------------------------------------------------------------
#
odbname = 'Job-1.odb'
odb = openOdb(odbname)
#
IncNum = len(odb.rootAssembly.instances) - 4
CoordField = odb.steps['Step-1'].frames[-1].fieldOutputs['COORD']
#
#-------------------------------------------------------------------------------------
#
f1 = open('NewCentroids.txt', 'w')	
f2 = open('NewOriangles.txt', 'w')	
#
for i in range(IncNum):	   
    Field1 = CoordField.getSubset(region=odb.rootAssembly.nodeSets['SET-'+str(i+1)+'-1'], position=NODAL)
    Field1Values = Field1.values[0].data #Double
    Field3 = CoordField.getSubset(region=odb.rootAssembly.nodeSets['SET-P-'+str(i+1)], position=NODAL)
    Field3Values = Field3.values[0].data #Double
    f1.write(str(Field3Values[0]) + ',' + str(Field3Values[1]) + '\n')
#
#-------------------------------------------------------------------------------------
#        
    Length = (Field1Values[0] - Field3Values[0])**2 + (Field1Values[1] - Field3Values[1])**2
    Length = Length**0.5
    Xv = (Field1Values[0] - Field3Values[0])/Length
    Yv = (Field1Values[1] - Field3Values[1])/Length
#        
    if Xv > 0 and  Yv >= 0:
        Phi = atan(Yv/Xv)/pi*180
    if Xv < 0 and  Yv >= 0:
        Phi = atan(Yv/Xv)/pi*180 + 180
    if Xv < 0 and  Yv < 0:
        Phi = 180 + atan(Yv/Xv)/pi*180
    if Xv > 0 and  Yv < 0:
        Phi = 360 + atan(Yv/Xv)/pi*180
    if Xv == 0 and  Yv > 0:
        Phi = 90
    if Xv == 0 and  Yv < 0:
        Phi = 270
    if Xv == 0 and  Yv == 0:
        Phi = 0             
    f2.write(str(Phi) + '\n')
#
f1.close()
f2.close()
#   
#-------------------------------------------------------------------------------------
#   
odb.close() 

