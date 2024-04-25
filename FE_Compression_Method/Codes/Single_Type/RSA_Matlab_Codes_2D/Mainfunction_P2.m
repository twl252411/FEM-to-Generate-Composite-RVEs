% Main function
clc;
clear;
tic
%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
%AreaMat = [113.097335529233, 116.524446900354, 116.406840417483, 114.281917066696, 114.739462015697, 114.508294442773, 113.490034610931, 115.538171837272, 115.593030485755];
%EqvRadius = [6.0, 8.4, 7.32598183048945, 6.88050865276332, 9.81495457622364, 7.77817459305202, 8.5, 8.3, 11.8368845160521];
%
IniL = 400; FinL = 200.0; % initial RVE size, final RVE size
Radius = 6.0*1.05*2.0; % Inclusion length, radius, volume fraction
NumInc = ceil(FinL^2*0.5/(113.097335529233));
NumInc2 = randi([6,8], 1, 2);
NumInc3 = 1;
NumInc1 = NumInc - sum(NumInc2) - NumInc3;

%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
Inclusion.orientation = zeros(NumInc,2);
for i = 1:NumInc
    direction = 2*(0.5-rand(1,2)); 
    Inclusion.orientation(i,1:2) = direction/norm(direction);        %fiber's orientation vectors
end
%
tau = 0.5;
Toler = 1E-20;  % Toleration
Id = [1 0; 0 1];
Oa = [0.5 0; 0 0.5];
PredA = Closureapproximation(Oa);
%
Iter = 1;
while Iter >= 1
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
%---------------------------------------------------------------------------------------------------------------------------------------------------------------    
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
%---------------------------------------------------------------------------------------------------------------------------------------------------------------   
    LastFunc = Funcx;
    for i = 1:NumInc
        Inclusion.orientation(i,1:2) = Inclusion.orientation(i,1:2) - tau*DPDX(i,1:2); 
        Inclusion.orientation(i,1:2) = Inclusion.orientation(i,1:2)/norm(Inclusion.orientation(i,1:2));
    end
%
end
LastA = Last2oritensor(Inclusion.orientation,NumInc);
%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
Geometry.Rvesize = [IniL, IniL] - Radius*2.0*ones(1,2);
Iteration = 1;
Inclusion.midpoint = [];
while Iteration <= NumInc1
    disp('No. of Inclusion =');
    disp(Iteration);
    IterRemark = 0;
%    
    CPts = zeros(1,2);
    CPts(1,1:2) = Geometry.Rvesize.*(0.5 - rand(1,2));
%
    NewInclusion.midpoint = CPts;
% 
    Num1 = size(Inclusion.midpoint,1);
%---------------------------------------------------------------------------------------------------------------------------------------   
    if Iteration == 1      
        Inclusion.midpoint = [Inclusion.midpoint; NewInclusion.midpoint];          
        IterRemark = 1;
%---------------------------------------------------------------------------------------------------------------------------------------        
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
%---------------------------------------------------------------------------------------------------------------------------------------               
        if Remark == 0
            Inclusion.midpoint = [Inclusion.midpoint; NewInclusion.midpoint];       
            IterRemark = 1; 
        end        
    end
%---------------------------------------------------------------------------------------------------------------------------------------   
    if IterRemark ==1
        Iteration = Iteration + 1;
    end
end
%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
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
        %---------------------------------------------------------------------------------------------------------------------------------------   
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
        %---------------------------------------------------------------------------------------------------------------------------------------  
        if IterRemark ==1
            Iteration = Iteration + 1;
        end
    end
    %---------------------------------------------------------------------------------------------------------------------------------------
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
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
L = FinL/2.0 + Radius*1.25;
Inclusion.midpoint2(2*sum(NumInc2)+1:2*sum(NumInc2)+4,1:2) = [L, L; L, -L; -L, -L; -L, L];
%
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
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
%--------------------------------------------------------------------------------------------------------------------------------------------------------------- 
%
writematrix(Inclusion.midpoint, 'C:\Temp\Midpoints.txt'); 
writematrix(Inclusion.midpoint2, 'C:\Temp\Midpoints2.txt'); 
writematrix(Inclusion.oriangle(1:NumInc1,:), 'C:\Temp\Oriangles.txt'); 
writematrix(Inclusion.oriangle(NumInc1+1:NumInc+sum(NumInc2)+3,:), 'C:\Temp\Oriangles2.txt'); 
writematrix(NumInc2, 'C:\Temp\NumPeriInc.txt'); 
