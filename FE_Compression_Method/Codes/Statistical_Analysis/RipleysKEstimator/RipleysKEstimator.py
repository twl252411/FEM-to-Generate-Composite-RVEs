#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from astropy.stats import RipleysKEstimator
#
Filnum, strname = 10, 'Star'
RLength, numrad = 200.0, 126
rad = np.linspace(0, RLength*5/8, numrad) 
RksE, RdfE = np.linspace(0, 0, numrad), np.linspace(0, 0, numrad-1)
#
for ifile in range(Filnum):
    #
    # RipleysK Function
    #
    points = np.loadtxt('C:\\Temp\\Generated_Points_Angles\\' + strname + '\\NewCentroids'+str(ifile+1)+'.txt', delimiter=',')
    ptnum = len(points)
    for ipt in range(ptnum-1,-1,-1):
        if abs(points[ipt][0]) > RLength/2.0 or abs(points[ipt][1]) > RLength/2.0:
            points = np.delete(points, ipt, 0)
    #
    Kest = RipleysKEstimator(area=RLength**2, x_max=RLength/2.0, y_max=RLength/2.0, x_min=-RLength/2.0, y_min=-RLength/2.0)
    Rks = Kest.Hfunction(data=points, radii=rad, mode='translation')
    RKF = Kest.evaluate(data=points, radii=rad, mode='translation')
    RksE = RksE + Rks/Filnum
    #
    if ifile == 0:
        ar = np.column_stack((rad, Rks))
    else:
        ar = np.column_stack((ar, Rks))
    #
    # Radial_Distribution
    #
    Rdf, rad1 = np.linspace(0, 0, numrad-1), np.linspace(0, 0, numrad-1)
    for j in range(numrad-1):
        rad1[j] = (rad[j]+rad[j+1])/2.0
        Rdf[j] = (RKF[j+1]-RKF[j])/(rad[j+1]-rad[j])*(1.0/(2*np.pi*rad1[j]))
    RdfE = RdfE + Rdf/Filnum
    #
    if ifile == 0:
        ar1 = np.column_stack((rad1, Rdf))
    else:
        ar1 = np.column_stack((ar1, Rdf))
#
ar, ar1 = np.column_stack((ar, RksE)), np.column_stack((ar1, RdfE))
#
writer = pd.ExcelWriter('C:\\Temp\\Statistical_Analysis\\RipleysKEstimator\\' + strname + '_RVE\\RipleysK_Radial_Distribution.xlsx')
pdata = pd.DataFrame(ar)
pdata.to_excel(writer, 'page-1', float_format='%.6f', header=None, index=False)
pdata = pd.DataFrame(ar1)
pdata.to_excel(writer, 'page-2', float_format='%.6f', header=None, index=False)
writer.close()
#