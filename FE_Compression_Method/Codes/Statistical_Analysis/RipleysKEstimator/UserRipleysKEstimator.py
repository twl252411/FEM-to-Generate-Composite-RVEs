#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
#
Rlength = 250.0
filenum, NumR, filename1 = 1, 126, 'C:\\Temp\\Generated_Points_Angles\\Circle\\RipleysK_Function.xlsx',
rad = np.linspace(0, 125, NumR)
#
points = np.loadtxt('C:\\Temp\\Generated_Points_Angles\\Circle\\Centroids8-3.txt', delimiter=',')
ptnum = len(points)
for ipt in range(ptnum-1,-1,-1):
    if abs(points[ipt][0]-Rlength/2.0) > Rlength/2.0 or abs(points[ipt][1]-Rlength/2.0) > Rlength/2.0:
        points = np.delete(points, ipt, 0)
#
nptnum = len(points)
ppoints = np.zeros((9*nptnum, 2))
for ipt in range(3):
    for jpt in range(3):
        ppoints[(jpt*3+ipt)*nptnum:(jpt*3+ipt+1)*nptnum] = points[:,0:2] + np.array([[(ipt-1)*Rlength, (1-jpt)*Rlength],])
#
results = np.zeros((NumR,nptnum))
#
for ipt in range(NumR):
    for jpt in range(9*nptnum):
        for kpt in range(nptnum):
            tmplen = np.linalg.norm(points[kpt,1:2]-ppoints[jpt])
            if tmplen < rad[ipt] or abs(tmplen-rad[ipt])<1E-3:
                results[ipt][kpt] = results[ipt][kpt] + Rlength**2/nptnum
#
RKS = np.average(results, axis=1)
