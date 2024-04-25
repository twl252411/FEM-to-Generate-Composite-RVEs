#
# Jupyter Notebook runs this code much more efficient
#
import numpy as np
from rdfpy import rdf
import pandas as pd
import matplotlib.pyplot as plt
#
points = np.loadtxt('C:\\Temp\\Generated_Points_Angles\\Circle\\Centroids8-3.txt', delimiter=',')
#
# compute radial distribution function with step size = 10.0
g_r, radii = rdf(points[:,0:2], dr=2.0)
#
plt.plot(radii,g_r)
plt.show()
#
pdata = pd.DataFrame(np.column_stack((radii, g_r)))
writer = pd.ExcelWriter('Rdf.xlsx')
pdata.to_excel(writer,'page_1',float_format='%.6f',header=None,index=False)
writer.close()