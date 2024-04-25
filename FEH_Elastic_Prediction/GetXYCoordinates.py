from abaqus import *
from abaqusConstants import *
import string
import random
#
class GetXYCoordinates:
    #
    def __init__(self, UserVariables):
        self.UserVariables = UserVariables
    #
    def Partition(self, PartName):
    	#
    	dPid = self.UserVariables['dPid']
    	#
    	p = mdb.models['Model-1'].parts[PartName]
    	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=0.0)
    	p = mdb.models['Model-1'].parts[PartName]
    	e = p.edges
    	pickedEdges = e[0:len(e)]
    	d = p.datums
    	p.PartitionEdgeByDatumPlane(datumPlane=d[dPid], edges=pickedEdges)
    #	
    def GetCoords(self, PartName):
    	p = mdb.models['Model-1'].parts[PartName]
    	for iver in p.vertices:
    	    if iver.pointOn[0][0] > 1.0E-4 and abs(iver.pointOn[0][1]) < 1.0E-4:
    	        Coord1  = iver.pointOn[0][0]
    	return Coord1