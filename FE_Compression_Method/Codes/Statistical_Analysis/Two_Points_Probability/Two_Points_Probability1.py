# <snippet>
import GooseEYE
import itertools
import numpy as np
import pandas as pd
#
FilId, Filnum, strname = 1, 1, 'Star'
RLength, Roi1, Roi2 = 200.0, int(400*1.732)+1, 401
NumEle1, NumEle2 = int((Roi1+1)/2), int((Roi2+1)/2)
Xline, Yline = np.linspace(0, RLength, NumEle1), np.linspace(0, RLength, NumEle2)
S2 = np.zeros((Roi1, Roi2))
#
#------------------------------------------------------------------------------
#
for ifl in range(Filnum):
    #
    Id = (FilId-1)*Filnum + ifl + 1
    data = np.loadtxt('C:\\Temp\\Statistical_Analysis\\Two_Points_Probability\\H6RVE.txt', dtype=int, delimiter=',')
    #
    phi = np.mean(data)
    S2Mat = GooseEYE.S2((Roi1, Roi2), data, data)
    S2 = S2 + S2Mat/Filnum
# #
# #----------------------------------- Save as an excel file -------------------------------
# #
# writer = pd.ExcelWriter("C:\\Temp\\Statistical_Analysis\\Two_Points_Probability\\H6RVE.xlsx")
# #
# #----------------------------------- 3D Contour -------------------------------
# #
# TPs2 = np.zeros((NumEle1*NumEle2,3))
# #
# for x, y in itertools.product(range(NumEle1), range(NumEle2)):
#     TPs2[x+y*NumEle1,0:3] = [Xline[x], Yline[y], S2[x+NumEle1-1,y+NumEle2-1]]
# #
# pdata = pd.DataFrame(TPs2)
# pdata.to_excel(writer, 'page_1', float_format='%.6f', header=None, index=False)
# #
# #-------------------------------- Different angles ----------------------------
# #
# TPori1 = np.zeros((NumEle2,4))       # 0
# for y in range(NumEle2):
#     TPori1[y,0:4] = [Xline[0], Yline[y], Yline[y], S2[NumEle1-1, y+NumEle2-1]]
# pdata = pd.DataFrame(TPori1)
# pdata.to_excel(writer, 'page_2', float_format='%.6f', header=None, index=False)
# #
# TPori2 = np.zeros((NumEle2,4))       # 45
# for y in range(NumEle2):
#     TPori2[y,0:4] = [Xline[y], Yline[y], np.linalg.norm([Xline[y],Yline[y]]), S2[y+NumEle1-1,y+NumEle2-1]]
# pdata = pd.DataFrame(TPori2)
# pdata.to_excel(writer, 'page_3', float_format='%.6f', header=None, index=False)
# #
# TPori3 = np.zeros((NumEle1,4))        # 90
# for x in range(NumEle1):
#     TPori3[x,0:4] = [Xline[x], Yline[0], Xline[x], S2[x+NumEle1-1, NumEle2-1]]
# pdata = pd.DataFrame(TPori3)
# pdata.to_excel(writer, 'page_4', float_format='%.6f', header=None, index=False)
# #
# #--------------------------------- Different Distance -------------------------
# #
# TPdis1 = [ ]   # 40
# for y in range(NumEle2):
#     for x in range(NumEle1):
#         if np.rint(np.linalg.norm([Xline[x],Yline[y]])) == 40.0:
#             if Yline[y] == 0:
#                 angle = 90.0
#             else:
#                 angle = np.arctan(Xline[x]/Yline[y])*180/np.pi
#             #
#             a1, a2 = S2[2*x+NumEle1-1,2*y+NumEle2-1], S2[3*x+NumEle1-1,3*y+NumEle2-1]
#             a3, a4 = S2[4*x+NumEle1-1,4*y+NumEle2-1], S2[5*x+NumEle1-1,5*y+NumEle2-1]
#             #
#             TPdis1.append([angle, Xline[x], Yline[y], S2[x+NumEle1-1,y+NumEle2-1], a1, a2, a3, a4])
#             break
# #
# TPdis2 = [ ]   # 40
# for x in range(NumEle1):
#     for y in range(NumEle2):
#         if np.rint(np.linalg.norm([Xline[x],Yline[y]])) == 40.0:
#             if Yline[y] == 0:
#                 angle = 90.0
#             else:
#                 angle = np.arctan(Xline[x]/Yline[y])*180/np.pi
#             #
#             a1, a2 = S2[2*x+NumEle1-1,2*y+NumEle2-1], S2[3*x+NumEle1-1,3*y+NumEle2-1]
#             a3, a4 = S2[4*x+NumEle1-1,4*y+NumEle2-1], S2[5*x+NumEle1-1,5*y+NumEle2-1]
#             #
#             TPdis2.append([angle, Xline[x], Yline[y], S2[x+NumEle1-1,y+NumEle2-1], a1, a2, a3, a4])
#             break
# #
# TPdis = np.concatenate((np.array(TPdis1), np.array(TPdis2)))
# TPdis = TPdis[np.argsort(TPdis[:,0])]
# TPdis = np.unique(TPdis,axis=0)
# #
# pdata = pd.DataFrame(TPdis)
# pdata.to_excel(writer, 'page_7', float_format='%.6f', header=None, index=False)
# #
# writer.close()
#
#--------------------------------- Different Distance -------------------------
#
writer = pd.ExcelWriter("C:\\Temp\\Statistical_Analysis\\Two_Points_Probability\\H6RVE1.xlsx")
#
TPori2 = np.zeros((NumEle2,4))       # 30
for y in range(NumEle2):
    TPori2[y,0:4] = [Xline[y],Yline[y], np.linalg.norm([Xline[y],Yline[y]]), S2[y+NumEle1-1,y+NumEle2-1]]
pdata = pd.DataFrame(TPori2)
pdata.to_excel(writer, 'page_5', float_format='%.6f', header=None, index=False)

TPori3 = np.zeros((int(NumEle1/3),4))     # 60
for x in range(int(NumEle1/3)):
    TPori3[x,0:4] = [Xline[3*x],Yline[x], np.linalg.norm([Xline[x*3],Yline[x]]), S2[x*3+NumEle1-1, x+NumEle2-1]]
pdata = pd.DataFrame(TPori3)
pdata.to_excel(writer, 'page_6', float_format='%.6f', header=None, index=False)
#
writer.close()
