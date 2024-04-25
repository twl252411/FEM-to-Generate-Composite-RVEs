#
import numpy as np
import pandas as pd
from scipy.spatial import Voronoi
from shapely.geometry import Polygon
#
def bounded_voronoi(bnd, pnts):
    #    
    gn_pnts = np.concatenate([pnts, np.array([[400, 400], [400, -400], [-400, 0]])])
    vor = Voronoi(gn_pnts)
    bnd_poly = Polygon(bnd)
    vor_polys = []
    #
    for i in range(len(gn_pnts) - 3):
        vor_poly = [vor.vertices[v] for v in vor.regions[vor.point_region[i]]]
        i_cell = bnd_poly.intersection(Polygon(vor_poly))
        vor_polys.append(list(i_cell.exterior.coords[:-1]))
    #
    areas = []
    for i in range(len(vor_polys)):
        points = vor_polys[i]
        sizep = len(vor_polys[i])
        area = points[-1][0] * points[0][1] - points[0][0] * points[-1][1]
        for j in range(1, sizep):
            v = j - 1
            area += (points[v][0] * points[j][1])
            area -= (points[j][0] * points[v][1])
        #
        areas.append(0.5 * abs(area))
    Area = np.array(areas)
    #
    MeanValue = np.mean(Area)
    StanValue = np.std(Area)
#
    return vor_polys, MeanValue, StanValue
#
#---------------------------------------------------------------------------------------------------------------
#
Filenum = 4
RLength, VcaMat = 200.0, np.zeros((Filenum,1))
bnd = np.array([[0, 0], [RLength, 0], [RLength, RLength], [0, RLength]])
for i in range(Filenum):
    filename = "C:\\Temp\\Generated_Points_Angles\\Multi\\NewCentroids" + str(i+1) + ".txt"
    points = np.loadtxt(filename, delimiter=',') + [RLength/2.0, RLength/2.0]
    ptnum = len(points)
    for ipt in range(ptnum-1,-1,-1):
        if abs(points[ipt][0]-RLength/2.0) > RLength/2.0 or abs(points[ipt][1]-RLength/2.0) > RLength/2.0:
            points = np.delete(points, ipt, 0)
    vor_polys, MeanValue, StanValue = bounded_voronoi(bnd, points)
    VcaMat[i,0] = StanValue/MeanValue
#
VcaMat = np.squeeze(VcaMat)
VcaMat.sort()
#
pdata = pd.DataFrame(VcaMat)
writer = pd.ExcelWriter("C:\\Temp\\Statistical_Analysis\\Voronoi_Cells_Area\\Multi_RVE\\Voronoi_Cells_Area_Ml.xlsx")
pdata.to_excel(writer, 'page-1', float_format='%.6f', header=None, index=False)
writer.close()
#




