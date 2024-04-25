% Main function
clc;
clear;
tic
%
%-------------------------------------------------------------------------------------------------
%
Inctype = 5; strname = 'Spolygon3';
%
if Inctype == 1
    %---Circles---361
    Incsize = 6.0; Numpt = 121;
elseif Inctype == 2
    %---Lobular2s---
    Incsize = 4.2; Numpt = 121;
elseif Inctype == 3
    %---Lobular3s---
    Incsize = 3.4; Numpt = 121;
elseif Inctype == 4
    %---Lobular4s---
    Incsize = 2.85; Numpt = 141;
elseif Inctype == 5
    %---Spolygon3s---
    Incsize = [17.0, 2.25]; Numpt = 124;
elseif Inctype == 6
    %---Spolygon4s---
    Incsize = [11.0, 2.75]; Numpt = 125;
elseif Inctype == 7
    %---Ellipses---
    Incsize = [8.5, 4.25]; Numpt = 121;
elseif Inctype ==8
    %---Kidneys---
    Incsize = [5.6, 8.3, 3.8, 5.8]; Numpt = 121;
else
    %---Stars---
    Incsize = [8.6, 2.0]; Numpt = 547;
end
%
LInclusion = GeometryLoc(Incsize, Numpt, Inctype); % Inclusion Shape Definition
plot(LInclusion(:,1), LInclusion(:,2)); axis equal;
%
%-------------------------------------------------------------------------------------------------
%
for ifile = 1:10
    %
    f1 = ['C:\Temp\Generated_Points_Angles\' strname '\NewCentroids' num2str(ifile) '.txt'];
    f2 = ['C:\Temp\Generated_Points_Angles\' strname '\NewOriangles' num2str(ifile) '.txt'];
    Incpoints = importdata(f1); 
    Incangs = importdata(f2);
    %
    NumInc = size(Incpoints, 1);
    nndist = zeros(NumInc, 2); 
    orivec = zeros(NumInc, 2);
    %
    for i = 1:NumInc
        %
        mindist = zeros(NumInc,1); 
        %
        for j = 1:NumInc
            if i ~= j
                P1 = IncTransform(Incangs(i,1), Incpoints(i,1:2), LInclusion);
                P2 = IncTransform(Incangs(j,1), Incpoints(j,1:2), LInclusion);
                mindist(j,1) = Mindist2Shape(P1, P2);  
            else
                mindist(j,1) = 200.0;
            end
        end
        %
        [nndist(i,1), Index] = min(mindist);
        %
        orivec(i,1:2) = (Incpoints(i,1:2) - Incpoints(j,1:2))/norm(Incpoints(i,1:2) - Incpoints(j,1:2));
        %
        for j = 1:NumInc
            if abs(mindist(j,1) - nndist(i,1)) < 1E-6
                mindist(j,1) = 200.0;
            end
        end
        %
        nndist(i,2) = min(mindist); 
        %
    end
    %
    nnangles = Vector2Angle(orivec);
    %
    f1 = ['C:\Temp\Statistical_Analysis\Nearest_Neighbour_Distance_Angle\' strname '_RVE\nndistance_' num2str(ifile) '.txt'];
    f2 = ['C:\Temp\Statistical_Analysis\Nearest_Neighbour_Distance_Angle\' strname '_RVE\nnangles_' num2str(ifile) '.txt'];
    writematrix(nndist, f1); 
    writematrix(nnangles, f2); 
end
