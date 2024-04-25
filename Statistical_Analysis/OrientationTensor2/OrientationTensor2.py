#!/usr/bin/env python
# coding: utf-8
import numpy as np
# 
a2 = np.zeros([2,2])
NInc = 281
myfile = open('NewOriangles.txt','r')
lines = myfile.readlines() 
pvec = np.zeros([NInc,2])
theta = np.zeros(NInc)
for i in range(NInc):
    ele = lines[i].split(',')
    theta[i] = float(ele[0])
    p = np.array([np.cos(theta[i]/180*np.pi), np.sin(theta[i]/180*np.pi)])
    pvec[i,:] = p[:]
    a2 = a2 + np.outer(p, p)/NInc
#
f = open('OrientationTensor2.txt', 'w')	
np.savetxt(f, a2)