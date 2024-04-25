function PointLoc = GeometryLoc(Incsize, Numpt, Flag)
    PointLoc = zeros(Numpt,2);
    %---Circle---
    if Flag == 1
        for j = 1:360
            theta = (j-1)*pi/180;
            PointLoc(j,1:2) = [Incsize*cos(theta), Incsize*sin(theta)];
        end
    end
    %---Lobular2s---
    if Flag == 2
        for j = 1:240
            theta = (j+60)*pi/180;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta)];   
            %
            theta = (j-120)*pi/180;
            PointLoc(j+300,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta)];     
        end
        for j = 1:60
            theta = (120-j)*pi/180;
            PointLoc(j+240,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - sqrt(3)*Incsize];     
            %
            theta = (300-j)*pi/180;
            PointLoc(j+540,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + sqrt(3)*Incsize];     
        end 
    end
    %---Lobular3s---
    if Flag == 3
        for j = 1:180
            theta = (j+120)*pi/180;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) - sqrt(3)/3.0*Incsize];
            %
            theta = (j-120)*pi/180;
            PointLoc(j+240,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) - sqrt(3)/3.0*Incsize]; 
            %
            theta = (j)*pi/180;
            PointLoc(j+480,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
        end 
        for j = 1:60
            theta = (120-j)*pi/180;
            PointLoc(j+180,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
            %
            theta = (240-j)*pi/180;
            PointLoc(j+420,1:2) = [Incsize*cos(theta) + 2*Incsize, Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
            %
            theta = (-j)*pi/180;
            PointLoc(j+660,1:2) = [Incsize*cos(theta) - 2*Incsize, Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
        end
    end
    %---Lobular4s---
    if Flag == 4
        for j = 1:150
            theta = (j+150)*pi/180;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) - Incsize];
            %
            theta = (j-120)*pi/180;
            PointLoc(j+210,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) - Incsize];  
            %
            theta = (j-30)*pi/180;
            PointLoc(j+420,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) + Incsize];
            %
            theta = (j+60)*pi/180;
            PointLoc(j+630,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) + Incsize];
       end
       for j = 1:60
            theta = (120-j)*pi/180;
            PointLoc(j+150,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - (1+sqrt(3))*Incsize]; 
            %
            theta = (210-j)*pi/180;
            PointLoc(j+360,1:2) = [Incsize*cos(theta)+(1+sqrt(3))*Incsize, Incsize*sin(theta)]; 
            %
            theta = (-60-j)*pi/180;
            PointLoc(j+570,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + (1+sqrt(3))*Incsize]; 
            %
            theta = (30-j)*pi/180;
            PointLoc(j+780,1:2) = [Incsize*cos(theta)- (1+sqrt(3))*Incsize, Incsize*sin(theta)]; 
        end
    end
    %---Spolygon3s---
    if Flag == 5
        b = Incsize(1,1) - 2*sqrt(3)*Incsize(1,2);
        for j = 1:121
            theta = (j+150-1)*pi/180;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) + Incsize(1,2)]; 
            %
            theta = (j-90-1)*pi/180;
            PointLoc(j+121,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) + Incsize(1,2)]; 
            %
            theta = (j+30-1)*pi/180;
            PointLoc(j+242,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) + sqrt(3)*Incsize(1,1)/2 - 2*Incsize(1,2)]; 
        end
            PointLoc(:,2) = PointLoc(:,2) - sqrt(3)/6.0*Incsize(1,1); 
    end
    %---Spolygon4s---
    if Flag == 6
        b = Incsize(1,1) - 2*Incsize(1,2);
        for j = 1:91
            theta = (j+180-1)*pi/180;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) - b/2]; 
            %
            theta = (j+270-1)*pi/180;
            PointLoc(j+91,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) - b/2]; 
            %   
            theta = (j-1)*pi/180;
            PointLoc(j+182,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) + b/2]; 
            %   
            theta = (j+90-1)*pi/180;
            PointLoc(j+273,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) + b/2]; 
        end
    end
    %---Ellipses---
    if Flag == 7
        for j = 1:Numpt
            theta = 2*j*pi/Numpt;
            PointLoc(j,1:2) = [Incsize(1,1)*cos(theta), Incsize(1,2)*sin(theta)];
        end
    end
    %---Kidneys---
    if Flag == 8
        R1 =  Incsize(1,1); R2 = Incsize(1,2); K1 = Incsize(1,3); a = Incsize(1,4);
        for j = 1:360
            theta = (j-1)*pi/180;
            PointLoc(j,1:2) = [R1*cos(theta) + K1*exp(-a*cos(theta) - a), R2*sin(theta)];
        end
    end
    %---Stars---
    if Flag == 9
        Incs = 2*sin(18*pi/180)*Incsize(1,1); 
        d = Incs/2/tan(18*pi/180) - Incsize(1,2)/sin(18*pi/180) + Incs/2/tan(36*pi/180);
        e = Incs/2/sin(36*pi/180) + Incsize(1,2)/cos(36*pi/180);
        for j = 1:145
            theta = (j + 162 - 1)*pi/180;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - d*cos(54*pi/180), Incsize(1,2)*sin(theta) - d*sin(54*pi/180)]; 
            %
            theta = (j - 126 - 1)*pi/180;
            PointLoc(j + 218,1:2) = [Incsize(1,2)*cos(theta) + d*cos(54*pi/180), Incsize(1,2)*sin(theta) - d*sin(54*pi/180)]; 
            %
            theta = (j - 54 - 1)*pi/180;
            PointLoc(j + 436,1:2) = [Incsize(1,2)*cos(theta) + d*cos(18*pi/180), Incsize(1,2)*sin(theta) + d*sin(18*pi/180)]; 
            %
            theta = (j + 18 - 1)*pi/180;
            PointLoc(j + 654,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) + d]; 
            %
            theta = (j + 90 - 1)*pi/180;
            PointLoc(j + 872,1:2) = [Incsize(1,2)*cos(theta) - d*cos(18*pi/180), Incsize(1,2)*sin(theta) + d*sin(18*pi/180)]; 
        end
        for j = 1:73
            theta = (126 - j - 1)*pi/180;
            PointLoc(j + 145,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) - e]; 
            %
            theta = (198 - j - 1)*pi/180;
            PointLoc(j + 363,1:2) = [Incsize(1,2)*cos(theta) + e*cos(18*pi/180), Incsize(1,2)*sin(theta) - e*sin(18*pi/180)]; 
            %
            theta = (270 - j - 1)*pi/180;
            PointLoc(j + 581,1:2) = [Incsize(1,2)*cos(theta) + e*cos(54*pi/180), Incsize(1,2)*sin(theta) + e*sin(54*pi/180)]; 
            %
            theta = (342 - j - 1)*pi/180;
            PointLoc(j + 799,1:2) = [Incsize(1,2)*cos(theta) - e*cos(54*pi/180), Incsize(1,2)*sin(theta) + e*sin(54*pi/180)]; 
            %
            theta = (54 - j - 1)*pi/180;
            PointLoc(j + 1017,1:2) = [Incsize(1,2)*cos(theta) - e*cos(18*pi/180), Incsize(1,2)*sin(theta) - e*sin(18*pi/180)]; 
        end
    end
    %------------
    PointLoc(Numpt,1:2) = PointLoc(1,1:2);
end