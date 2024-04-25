from abaqus import *
from abaqusConstants import *
import string
import random
#
class GeometryShape2D:
    #
    def __init__(self, UserVariables):
        self.UserVariables = UserVariables
    #
    def Circles(self, PartName):
        #-----Parameters-----
        Radius, Type = self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(Radius, 0.0))
        # 
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Lobular2s(self, PartName):
    	#-----Parameters-----
        Radius, Type = self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.ArcByCenterEnds(center=(-Radius, 0.0), point1=(-Radius/2, Radius/2*sqrt(3)), point2=(-Radius/2, -Radius/2*sqrt(3)), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(0.0, -Radius*sqrt(3)), point1=(-Radius/2, -Radius/2*sqrt(3)), point2=(Radius/2, -Radius/2*sqrt(3)), direction=CLOCKWISE)
        s.ArcByCenterEnds(center=(Radius, 0.0), point1=(Radius/2, -Radius/2*sqrt(3)), point2=(Radius/2, Radius/2*sqrt(3)), direction=COUNTERCLOCKWISE)      
        s.ArcByCenterEnds(center=(0.0, Radius*sqrt(3)), point1=(Radius/2, Radius/2*sqrt(3)), point2=(-Radius/2, Radius/2*sqrt(3)), direction=CLOCKWISE)
        #
        if Type == 'DEFORMABLE_BODY':          
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Lobular3s(self, PartName):
    	#-----Parameters-----
        Radius, Type = self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.ArcByCenterEnds(center=(-Radius, 0.0 - sqrt(3)/3.0*Radius), point1=(-Radius*3.0/2, Radius/2.0*sqrt(3)- sqrt(3)/3.0*Radius), point2=(-Radius/2, 
            -Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(0.0,-Radius*sqrt(3)- sqrt(3)/3.0*Radius), point1=(-Radius/2, -Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), point2=(Radius/2, 
            -Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), direction=CLOCKWISE)    
        s.ArcByCenterEnds(center=(Radius, 0.0- sqrt(3)/3.0*Radius), point1=(Radius/2, -Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), point2=(Radius*3.0/2, 
            Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(2.0*Radius, Radius*sqrt(3)- sqrt(3)/3.0*Radius), point1=(Radius*3.0/2, Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), point2=(Radius, 
            Radius*sqrt(3)- sqrt(3)/3.0*Radius), direction=CLOCKWISE)     
        s.ArcByCenterEnds(center=(0.0, Radius*sqrt(3)- sqrt(3)/3.0*Radius), point1=(Radius, Radius*sqrt(3)- sqrt(3)/3.0*Radius), point2=(-Radius, 
            Radius*sqrt(3)- sqrt(3)/3.0*Radius), direction=COUNTERCLOCKWISE)     
        s.ArcByCenterEnds(center=(-2.0*Radius, Radius*sqrt(3)- sqrt(3)/3.0*Radius), point1=(-Radius, Radius*sqrt(3)- sqrt(3)/3.0*Radius), point2=(-Radius*3.0/2, 
            Radius/2*sqrt(3)- sqrt(3)/3.0*Radius), direction=CLOCKWISE) 
        #         
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Lobular4s(self, PartName):
    	#-----Parameters-----
        Radius, Type = self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.ArcByCenterEnds(center=(-Radius, Radius), point1=(-Radius/2, Radius*(1+sqrt(3)/2)), point2=(-Radius*(1+sqrt(3)/2), Radius/2), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(-Radius*(1+sqrt(3)), 0.0), point1=(-Radius*(1+sqrt(3)/2), Radius/2), point2=(-Radius*(1+sqrt(3)/2), -Radius/2),direction=CLOCKWISE)    
        s.ArcByCenterEnds(center=(-Radius, -Radius), point1=(-Radius*(1+sqrt(3)/2), -Radius/2), point2=(-Radius/2, -Radius*(1+sqrt(3)/2)), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(0.0, -Radius*(1+sqrt(3))), point1=(-Radius/2, -Radius*(1+sqrt(3)/2)), point2=(Radius/2, -Radius*(1+sqrt(3)/2)), direction=CLOCKWISE) 
        s.ArcByCenterEnds(center=(Radius, -Radius), point1=(Radius/2, -Radius*(1+sqrt(3)/2)), point2=(Radius*(1+sqrt(3)/2), -Radius/2), direction=COUNTERCLOCKWISE)
        s.ArcByCenterEnds(center=(Radius*(1+sqrt(3)), 0.0), point1=(Radius*(1+sqrt(3)/2), -Radius/2), point2=(Radius*(1+sqrt(3)/2), Radius/2),direction=CLOCKWISE)    
        s.ArcByCenterEnds(center=(Radius, Radius), point1=(Radius*(1+sqrt(3)/2), Radius/2), point2=(Radius/2, Radius*(1+sqrt(3)/2)), direction=COUNTERCLOCKWISE)    
        s.ArcByCenterEnds(center=(0.0, Radius*(1+sqrt(3))), point1=(Radius/2, Radius*(1+sqrt(3)/2)), point2=(-Radius/2, Radius*(1+sqrt(3)/2)), direction=CLOCKWISE)    
        #         
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Spolygon3s(self, PartName):
    	#-----Parameters-----
        Slength, Radius, Type = self.UserVariables['Slength'], self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        #
        pt1 = (-Slength/2.0 + Radius*sqrt(3),     -Slength*sqrt(3)/6.0)
        pt2 = ( Slength/2.0 - Radius*sqrt(3),     -Slength*sqrt(3)/6.0)
        pt3 = ( Slength/2.0 - Radius*sqrt(3)/2.0, -Slength*sqrt(3)/6.0 + Radius*3/2.0)
        pt4 = ( 0.0 + Radius*sqrt(3)/2.0,          Slength/3.0*sqrt(3) - Radius*3/2.0)
        pt5 = ( 0.0 - Radius*sqrt(3)/2.0,          Slength/3.0*sqrt(3) - Radius*3/2.0)
        pt6 = (-Slength/2.0 + Radius*sqrt(3)/2.0, -Slength*sqrt(3)/6.0 + Radius*3/2.0)
        #
        s.Line(point1=pt1, point2=pt2)
        s.ArcByCenterEnds(center=(pt2[0],pt2[1]+Radius), point1=pt2, point2=pt3, direction=COUNTERCLOCKWISE)   
        s.Line(point1=pt3, point2=pt4)
        s.ArcByCenterEnds(center=(0.0,Slength/3.0*sqrt(3)-2*Radius), point1=pt4, point2=pt5, direction=COUNTERCLOCKWISE)   
        s.Line(point1=pt5, point2=pt6)
        s.ArcByCenterEnds(center=(pt1[0],pt1[1]+Radius), point1=pt6, point2=pt1, direction=COUNTERCLOCKWISE)   
        #         
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Spolygon4s(self, PartName):
    	#-----Parameters-----
        Slength, Radius, Type = self.UserVariables['Slength'], self.UserVariables['Radius'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        #
        pt1 = (Slength/2.0, Slength/2.0 - Radius)
        pt2 = (Slength/2.0 - Radius, Slength/2.0)
        pt3 = (-Slength/2.0 + Radius, Slength/2.0)
        pt4 = (-Slength/2.0, Slength/2.0 - Radius)
        pt5 = (-Slength/2.0, -Slength/2.0 + Radius)
        pt6 = (-Slength/2.0 + Radius, -Slength/2.0)
        pt7 = (Slength/2.0 - Radius, -Slength/2.0)
        pt8 = (Slength/2.0, -Slength/2.0 + Radius)
        #
        s.Line(point1=pt8, point2=pt1)
        s.ArcByCenterEnds(center=(Slength/2.0-Radius,Slength/2.0-Radius), point1=pt1, point2=pt2, direction=COUNTERCLOCKWISE)   
        s.Line(point1=pt2, point2=pt3)
        s.ArcByCenterEnds(center=(-Slength/2.0+Radius,Slength/2.0-Radius), point1=pt3, point2=pt4, direction=COUNTERCLOCKWISE)  
        s.Line(point1=pt4, point2=pt5)
        s.ArcByCenterEnds(center=(-Slength/2.0+Radius,-Slength/2.0+Radius), point1=pt5, point2=pt6, direction=COUNTERCLOCKWISE)  
        s.Line(point1=pt6, point2=pt7)
        s.ArcByCenterEnds(center=(Slength/2.0-Radius,-Slength/2.0+Radius), point1=pt7, point2=pt8, direction=COUNTERCLOCKWISE)  
        #         
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']
    #
    def Ellipses(self, PartName):
    	#-----Parameters-----
        Axis1, Axis2, Type = self.UserVariables['Axis1'], self.UserVariables['Axis2'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(Axis1, 0.0), axisPoint2=(0.0, Axis2))
        #
        if Type == 'DEFORMABLE_BODY':
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']                    
    #
    def Kidneys(self, PartName):
    	#-----Parameters-----
        R1, R2, K1, a, Type = self.UserVariables['R1'], self.UserVariables['R2'], self.UserVariables['K1'], self.UserVariables['a'], self.UserVariables['Type']
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        points = []
        for ith in range(361):
            points = points + [(R1*cos(ith/180.0*pi) + K1*exp(-a*cos(ith/180.0*pi)-a), R2*sin(ith/180.0*pi))]
        s.Spline(points=points)
        #         
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__'] 
    #
    def F5stars(self, PartName):
    	#-----Parameters-----
        Alength, Radius, Type = self.UserVariables['Alength'], self.UserVariables['Radius'], self.UserVariables['Type']
        #
        Tlen = Alength*sin(18.0/180*pi)*tan(54.0/180*pi)
        #
        point1 = [Alength + Alength*sin(18.0/180*pi), 0.0 + Tlen]
        point2 = [Alength*sin(18.0/180*pi), 0.0 + Tlen]
        point3 = [0.0, Alength*cos(18.0/180*pi) + Tlen]
        point4 = [-Alength*sin(18.0/180*pi), 0.0 + Tlen]
        point5 = [-Alength - Alength*sin(18.0/180*pi), 0.0 + Tlen]
        point6 = [-2.0*Alength*sin(18.0/180*pi)*cos(36.0/180*pi), -Alength*sin(36.0/180*pi) + Tlen]
        point7 = [-Alength*cos(36.0/180*pi), -2.0*Alength*sin(36.0/180*pi)*(1+sin(18.0/180*pi)) + Tlen]
        point8 = [0.0, -Alength*sin(36.0/180*pi)*(1+2*sin(18.0/180*pi)) + Tlen]
        point9 = [Alength*cos(36.0/180*pi), -2.0*Alength*sin(36.0/180*pi)*(1+sin(18.0/180*pi)) + Tlen]
        point10 = [2.0*Alength*sin(18.0/180*pi)*cos(36.0/180*pi), -Alength*sin(36.0/180*pi) + Tlen]
        #
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.Line(point1=point1, point2=point2)
        s.Line(point1=point2, point2=point3)
        s.Line(point1=point3, point2=point4)
        s.Line(point1=point4, point2=point5)
        s.Line(point1=point5, point2=point6)
        s.Line(point1=point6, point2=point7)
        s.Line(point1=point7, point2=point8)
        s.Line(point1=point8, point2=point9)
        s.Line(point1=point9, point2=point10)
        s.Line(point1=point10, point2=point1)
        #
        s.FilletByRadius(radius=Radius, curve1=g[11], nearPoint1=(point1[0]-0.1,point1[1]-0.1), curve2=g[2], nearPoint2=(point1[0]-0.1,point1[1]-0.1))
        s.FilletByRadius(radius=Radius, curve1=g[2], nearPoint1=(point2[0]+0.1,point2[1]+0.1), curve2=g[3], nearPoint2=(point2[0]+0.1,point2[1]+0.1))
        s.FilletByRadius(radius=Radius, curve1=g[3], nearPoint1=(point3[0],point3[1]-0.1), curve2=g[4], nearPoint2=(point3[0],point3[1]-0.1))
        s.FilletByRadius(radius=Radius, curve1=g[4], nearPoint1=(point4[0]-0.1,point4[1]+0.1), curve2=g[5], nearPoint2=(point4[0]-0.1,point4[1]+0.1))
        s.FilletByRadius(radius=Radius, curve1=g[5], nearPoint1=(point5[0]+0.1,point5[1]-0.1), curve2=g[6], nearPoint2=(point5[0]+0.1,point5[1]-0.1))
        s.FilletByRadius(radius=Radius, curve1=g[6], nearPoint1=(point6[0]-0.1,point6[1]-0.1), curve2=g[7], nearPoint2=(point6[0]-0.1,point6[1]-0.1))
        s.FilletByRadius(radius=Radius, curve1=g[7], nearPoint1=(point7[0]+0.1,point7[1]+0.1), curve2=g[8], nearPoint2=(point7[0]+0.1,point7[1]+0.1))
        s.FilletByRadius(radius=Radius, curve1=g[8], nearPoint1=(point8[0],point8[1]-0.1), curve2=g[9], nearPoint2=(point8[0],point8[1]-0.1))
        s.FilletByRadius(radius=Radius, curve1=g[9], nearPoint1=(point9[0]-0.1,point9[1]+0.1), curve2=g[10], nearPoint2=(point9[0]-0.1,point9[1]+0.1))
        s.FilletByRadius(radius=Radius, curve1=g[10], nearPoint1=(point10[0]+0.1,point10[1]-0.1), curve2=g[11], nearPoint2=(point10[0]+0.1,point10[1]-0.1))
        #       
        if Type == 'DEFORMABLE_BODY':  
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseShell(sketch=s)
        #
        if Type == 'DISCRETE_RIGID_SURFACE':           
            p = mdb.models['Model-1'].Part(name=PartName, dimensionality=TWO_D_PLANAR, type=DISCRETE_RIGID_SURFACE)
            p = mdb.models['Model-1'].parts[PartName]
            p.BaseWire(sketch=s)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']  