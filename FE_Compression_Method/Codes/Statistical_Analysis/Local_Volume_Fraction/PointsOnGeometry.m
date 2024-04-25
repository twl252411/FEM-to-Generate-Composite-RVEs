clear;
clc;
%
Points = importdata('NewCentroids1.txt');
Angles = importdata('NewOriangles1.txt');
NumInc = size(Points,1);
%
%---Circles---361
%Incsize =6.0; Numpt = 361;
%---Lobular2s---
%Incsize = 3.0; Numpt = 601;
%---Lobular3s---
% Incsize = 2.25; Numpt = 721;
%---Lobular4s---
% Incsize = 2.0; Numpt = 841;
%---Spolygon3s---
 Incsize = [17, 2.25]; Numpt = 364;
%---Spolygon4s---
% Incsize = [7.5, 1.5]; Numpt =365;
%---Ellipses---
% Incsize = [6, 3]; Numpt =361;
%---Kidneys---
%Incsize = [5.5, 8.2, 3.78, 5.76]; Numpt =361;
%---Stars---
%Incsize = [5.5, 1.0]; Numpt =1090;
PointLoc = GeometryLoc(Incsize, Numpt,5);
plot(PointLoc(:,1),PointLoc(:,2)); axis equal;
%
PointInc = zeros(Numpt, 2*NumInc);
for i = 1:NumInc
    phi = Angles(i,1)*pi/180;
    R = [cos(phi), -sin(phi); sin(phi), cos(phi)];
    for j = 1:Numpt
        Temp = R*(PointLoc(j,1:2))';
        PointInc(j,(i-1)*2+1:(i-1)*2+2) = Points(i,1:2) + Temp';
    end
end
%
writematrix(PointInc, 'OriginPoints.txt'); 
