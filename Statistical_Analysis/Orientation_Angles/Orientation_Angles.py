#
import numpy as np
import pandas as pd
import openpyxl
#
strname = 'Star'
points = np.loadtxt('C:\\Temp\\Generated_Points_Angles\\' + strname + '\\NewCentroids1.txt', delimiter=',')
angles = np.loadtxt('C:\\Temp\\Generated_Points_Angles\\' + strname + '\\NewOriangles1.txt', delimiter=',')
length = np.linalg.norm(points, axis=1)

data = np.concatenate((angles.reshape(len(angles),1), length.reshape(len(angles),1)), axis=1)
#
pdata = pd.DataFrame(data)
writer = pd.ExcelWriter("C:\\Temp\\"+strname+"_Orientation.xlsx")
pdata.to_excel(writer, 'page-1', float_format='%.6f', header=None, index=False)
writer.close()
#




