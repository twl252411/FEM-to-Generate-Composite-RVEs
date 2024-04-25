from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import string
#
TranVec = []
#
myfile = open('NewCentroids.txt','r')
lines = myfile.readlines()
for iline in lines:
    ele = string.split(iline,',')
    TranVec.append((float(ele[0]),float(ele[1])))	
#   
myfile = open('Midpoints2.txt','r')
lines = myfile.readlines()
for iline in lines:
    ele = string.split(iline,',')
    TranVec.append((float(ele[0]),float(ele[1])))	
#
f1 = open('NewCentroids.txt', 'w')	
for i in range(len(TranVec)):	   
    f1.write(str(TranVec[i][0]) + ',' + str(TranVec[i][1]) + '\n')
f1.close()
#
Angle = []
#
myfile = open('NewOriangles.txt','r')
lines = myfile.readlines()
a = len(lines)
for iline in lines:
    ele = string.split(iline,',')
    Angle.append((float(ele[0])))	
#   
myfile = open('Oriangles2.txt','r')
lines = myfile.readlines()
for iline in lines:
    ele = string.split(iline,',')
    Angle.append((float(ele[0])))	
#
f2 = open('NewOriangles.txt', 'w')	
for i in range(len(Angle)):
	f2.write(str(Angle[i]) + '\n')
f2.close()