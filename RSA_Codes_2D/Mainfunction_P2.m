% Main function
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%%%%
%%%% The function generates circumcenters of inclusions and the predefined orientation angles
%%%%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
clc;
clear;
%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
AreaMat = [113.097, 116.524, 116.407, 114.282, 114.739, 114.51, 113.490, 115.538, 115.593];  % Array for storing areas of 9 inclusions
EqvRadius = [6.0, 8.4, 7.326, 6.881, 9.815, 7.778, 8.5, 8.3, 11.837];                                            % Circumcenters of 9 inclusions
%
IniL = 400; FinL = 200.0; % Sizes of initial and final RVEs
Radius = EqvRadius(1,1)*1.05;  % Enlarge inclusions for ensuring the minimum seperation distance
NumInc = ceil(FinL^2*0.65/AreaMat(1,1)); % Total number of inclusions
NumInc2 = randi([6,7], 1, 2); % Numbers of periodic inclusions on edges of RVEs along two directions
NumInc3 = 1; % Number of inclusions located on the cornors of RVEs
NumInc1 = NumInc - sum(NumInc2) - NumInc3; % Number of sparse inclusions

%
%------------------------------------------------------------- Predefine inclusion orientation tensor --------------------------------------------------- 
%
Inclusion.orientation = zeros(NumInc,2);
for i = 1:NumInc
    direction = 2*(0.5-rand(1,2)); 
    Inclusion.orientation(i,1:2) = direction/norm(direction);        %fiber's orientation vectors
end
%
tau = 0.5;  Toler = 1E-20;  % Toleration
Id = [1 0; 0 1]; Oa = [0.5 0; 0 0.5]; % Predefined orientation tensor
PredA = Closureapproximation(Oa);
%
Iter = 1;
while Iter >= 1
    %
    disp('No. of Iteration ='); disp(Iter); Iter = Iter + 1;
    %
    LastA = Last4oritensor(Inclusion.orientation,NumInc);
    TempA = PredA - LastA;
    %
    Funcx = 0;
    for i = 1:2
        for j = 1:2
            for k = 1:2
                for l = 1:2
                        Funcx = Funcx + TempA(i,j,k,l)^2;
                end
            end
        end
    end
    %
    disp('Funcx = '); disp(Funcx);
    %
    if Funcx < Toler
        break;
    end
%------------------------------------------------------------
    DPDX = zeros(NumInc,2);    
    for i = 1:NumInc
        Temp1 = zeros(2,2);
        for ii = 1:2
            for jj = 1:2
                Temp1(ii,jj) = -Id(ii,jj) + Inclusion.orientation(i,ii)*Inclusion.orientation(i,jj);
            end
        end
        %
        Temp2 = zeros(2,2,2);
        for ii = 1:2
            for jj =1:2
                for kk = 1:2
                    Temp2(ii,jj,kk) = Inclusion.orientation(i,ii)*Inclusion.orientation(i,jj)*Inclusion.orientation(i,kk);
                end
            end
        end
        %
        Temp3 = zeros(1,2);
        for ii = 1:2
            for jj = 1:2
                for kk =1:2
                    for ll = 1:2
                        Temp3(1,ii) = Temp3(1,ii) + TempA(ii,jj,kk,ll)*Temp2(ll,kk,jj);
                    end
                end
            end
        end               
        %      
        DPDX(i,:) = Temp1*Temp3';                 
    end   
%------------------------------------------------------------
    LastFunc = Funcx;
    for i = 1:NumInc
        Inclusion.orientation(i,1:2) = Inclusion.orientation(i,1:2) - tau*DPDX(i,1:2); 
        Inclusion.orientation(i,1:2) = Inclusion.orientation(i,1:2)/norm(Inclusion.orientation(i,1:2));
    end
%
end
%
%---------------------------------------------------------- Generate circumcenters of sparse inclusions ---------------------------------------------------- 
%
Geometry.Rvesize = [IniL, IniL] - Radius*2.0*ones(1,2);
Iteration = 1;
Inclusion.midpoint = [];
while Iteration <= NumInc1
    disp('No. of Inclusion ='); disp(Iteration);
    IterRemark = 0;
%    
    CPts = zeros(1,2);
    CPts(1,1:2) = Geometry.Rvesize.*(0.5 - rand(1,2));
%
    NewInclusion.midpoint = CPts;
    Num1 = size(Inclusion.midpoint,1);
%------------------------------------------
    if Iteration == 1      
        Inclusion.midpoint = [Inclusion.midpoint; NewInclusion.midpoint];          
        IterRemark = 1;
%---------------------------------------      
    else  
        Remark = 0;                                         
        for i = 1:Num1                
            Dist = norm(NewInclusion.midpoint(1,1:2) - Inclusion.midpoint(i,1:2));                 
            if Dist <= 2*Radius
                Remark = 1;
                break;
            end
            if Remark == 1
                break;
            end                      
        end
%---------------------------------------
        if Remark == 0
            Inclusion.midpoint = [Inclusion.midpoint; NewInclusion.midpoint];       
            IterRemark = 1; 
        end        
    end
%---------------------------------------   
    if IterRemark ==1
        Iteration = Iteration + 1;
    end
end
%
%---------------------------------------------------------- Generate circumcenters of periodic inclusions ---------------------------------------------------- 
%
Rvesize = FinL - 2*Radius; 
L = FinL/2.0 + Radius*1.25;
Inclusion.midpoint2 = zeros(2*sum(NumInc2)+4, 2);
%  
for iii = 1:2
    Iteration = 1;
    midpoint = [];
    while Iteration <= NumInc2(1, iii)
        IterRemark = 0;
        %    
        Nmidpoint = Rvesize*(0.5 - rand());
        %
        Num1 = size(midpoint,1);
        %---------------------------------------  
        if Iteration == 1 
            midpoint = [midpoint; Nmidpoint];
            IterRemark = 1;     
        else        
            Remark = 0;
            for i = 1:Num1                       
                Distance =  norm(midpoint(i,1) - Nmidpoint);    
                if Distance <= Radius*2.0
                    Remark = 1;
                    break;
                end             
                if Remark == 1
                    break;
                end                       
            end         
            if Remark == 0
                midpoint = [midpoint; Nmidpoint];
                IterRemark = 1;
            end        
        end
        %----------------------------------------
        if IterRemark ==1
            Iteration = Iteration + 1;
        end
    end
    %----------------------------------------
    pii = sum(NumInc2);
    if iii == 1
        Inclusion.midpoint2(1:NumInc2(1,1), 1:2) = [L*ones(NumInc2(1,1),1), midpoint(:,1)];
        Inclusion.midpoint2(pii+1:pii+NumInc2(1,1), 1:2) = [-L*ones(NumInc2(1,1),1), midpoint(:,1)];
    else
        Inclusion.midpoint2(NumInc2(1,1)+1:sum(NumInc2(1,1:2)), 1:2) = [midpoint(:,1), L*ones(NumInc2(1,2),1)];
        Inclusion.midpoint2(pii+NumInc2(1,1)+1:pii+sum(NumInc2(1,1:2)), 1:2) = [midpoint(:,1), -L*ones(NumInc2(1,2),1)];
    end
end
%
%------------------------------------------
%
L = FinL/2.0 + Radius*1.25;
Inclusion.midpoint2(2*sum(NumInc2)+1:2*sum(NumInc2)+4,1:2) = [L, L; L, -L; -L, -L; -L, L];
%
%----------------------------------------------------------------Acquire inclusion orientation angles ------------------------------------------------------- 
%
Inclusion.oriangle = zeros(NumInc+sum(NumInc2)+3,1);
for i = 1:NumInc+sum(NumInc2)+3
    if i <= NumInc-1
        Xv = Inclusion.orientation(i,1); 
        Yv = Inclusion.orientation(i,2); 
    elseif i <= NumInc+sum(NumInc2)-1
        Xv = Inclusion.orientation(i-sum(NumInc2), 1); 
        Yv = Inclusion.orientation(i-sum(NumInc2), 2); 
    else
        Xv = Inclusion.orientation(NumInc, 1); 
        Yv = Inclusion.orientation(NumInc, 2); 
    end
%    
    if Yv >= 0
       Inclusion.oriangle(i,1) = acos(Xv)/pi*180;
    end
    if Yv < 0
        Inclusion.oriangle(i,1) = 360 - acos(Xv)/pi*180;
    end
    if Xv == 0 &&  Yv > 0
        Inclusion.oriangle(i,1) = 90;
    end
    if Xv == 0 &&  Yv < 0
        Inclusion.oriangle(i,1) = 270;
    end  
end
%
%---------------------------------------------------------Output the files of------------------------------------------------------------ 
%
writematrix(Inclusion.midpoint, 'Midpoints.txt');  % The txt file contains circumcenters of sparse inclusions
writematrix(Inclusion.midpoint2, 'Midpoints2.txt');  % The txt file contains circumcenters of periodic inclusions
writematrix(Inclusion.oriangle(1:NumInc1,:), 'Oriangles.txt');  % The txt file contains orientation angles of sparse inclusions
writematrix(Inclusion.oriangle(NumInc1+1:NumInc+sum(NumInc2)+3,:), 'Oriangles2.txt');  % The txt file contains orientation angles of periodic inclusions
writematrix(NumInc2, 'NumPeriInc.txt');  % The txt file contains numbers of periodic inclusions on edges of RVEs along two directions
