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
for ifile in range(0,18):
    jobname = 'Job-'+str(ifile+1)
    #
    mdb.JobFromInputFile(name=jobname, inputFileName=jobname+'.inp', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, 
        queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
        nodalOutputPrecision=SINGLE, userSubroutine='', scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8, 
        numDomains=8, numGPUs=0)
    mdb.jobs[jobname].submit(consistencyChecking=OFF)
    mdb.jobs[jobname].waitForCompletion()