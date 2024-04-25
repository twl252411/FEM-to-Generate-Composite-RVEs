function PointLoc = GeometryLoc(Incsize, Numpt, Flag)
    PointLoc = zeros(Numpt,2);
    %---Circle---
    if Flag == 1
        for j = 1:120
            theta = (j-1)*pi/60;
            PointLoc(j,1:2) = [Incsize*cos(theta), Incsize*sin(theta)];
        end
    end
    %---Lobular2s---
    if Flag == 2
        for j = 1:48
            theta = (j+12)*pi/36;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta)];   
            %
            theta = (j-24)*pi/36;
            PointLoc(j+60,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta)];     
        end
        for j = 1:12
            theta = (24-j)*pi/36;
            PointLoc(j+48,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - sqrt(3)*Incsize];     
            %
            theta = (60-j)*pi/36;
            PointLoc(j+108,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + sqrt(3)*Incsize];     
        end 
    end
    %---Lobular3s---
    if Flag == 3
        for j = 1:30
            theta = (j+20)*pi/30;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) - sqrt(3)/3.0*Incsize];
            %
            theta = (j-20)*pi/30;
            PointLoc(j+40,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) - sqrt(3)/3.0*Incsize]; 
            %
            theta = (j)*pi/30;
            PointLoc(j+80,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
        end 
        for j = 1:10
            theta = (20-j)*pi/30;
            PointLoc(j+30,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
            %
            theta = (40-j)*pi/30;
            PointLoc(j+70,1:2) = [Incsize*cos(theta) + 2*Incsize, Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
            %
            theta = (-j)*pi/30;
            PointLoc(j+110,1:2) = [Incsize*cos(theta) - 2*Incsize, Incsize*sin(theta) + sqrt(3)*Incsize - sqrt(3)/3.0*Incsize];     
        end
    end
    %---Lobular4s---
    if Flag == 4
        for j = 1:25
            theta = (j+25)*pi/30;
            PointLoc(j,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) - Incsize];
            %
            theta = (j-20)*pi/30;
            PointLoc(j+35,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) - Incsize];  
            %
            theta = (j-5)*pi/30;
            PointLoc(j+70,1:2) = [Incsize*cos(theta) + Incsize, Incsize*sin(theta) + Incsize];
            %
            theta = (j+10)*pi/30;
            PointLoc(j+105,1:2) = [Incsize*cos(theta) - Incsize, Incsize*sin(theta) + Incsize];
       end
       for j = 1:10
            theta = (20-j)*pi/30;
            PointLoc(j+25,1:2) = [Incsize*cos(theta), Incsize*sin(theta) - (1+sqrt(3))*Incsize]; 
            %
            theta = (35-j)*pi/30;
            PointLoc(j+60,1:2) = [Incsize*cos(theta)+(1+sqrt(3))*Incsize, Incsize*sin(theta)]; 
            %
            theta = (-10-j)*pi/30;
            PointLoc(j+95,1:2) = [Incsize*cos(theta), Incsize*sin(theta) + (1+sqrt(3))*Incsize]; 
            %
            theta = (5-j)*pi/30;
            PointLoc(j+130,1:2) = [Incsize*cos(theta)- (1+sqrt(3))*Incsize, Incsize*sin(theta)]; 
        end
    end
    %---Spolygon3s---
    if Flag == 5
        b = Incsize(1,1) - 2*sqrt(3)*Incsize(1,2);
        for j = 1:41
            theta = (j+50-1)*pi/60;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) + Incsize(1,2)]; 
            %
            theta = (j-30-1)*pi/60;
            PointLoc(j+41,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) + Incsize(1,2)]; 
            %
            theta = (j+10-1)*pi/60;
            PointLoc(j+82,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) + sqrt(3)*Incsize(1,1)/2 - 2*Incsize(1,2)]; 
        end
            PointLoc(:,2) = PointLoc(:,2) - sqrt(3)/6.0*Incsize(1,1); 
    end
    %---Spolygon4s---
    if Flag == 6
        b = Incsize(1,1) - 2*Incsize(1,2);
        for j = 1:31
            theta = (j+60-1)*pi/60;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) - b/2]; 
            %
            theta = (j+90-1)*pi/60;
            PointLoc(j+31,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) - b/2]; 
            %   
            theta = (j-1)*pi/60;
            PointLoc(j+62,1:2) = [Incsize(1,2)*cos(theta) + b/2, Incsize(1,2)*sin(theta) + b/2]; 
            %   
            theta = (j+30-1)*pi/60;
            PointLoc(j+93,1:2) = [Incsize(1,2)*cos(theta) - b/2, Incsize(1,2)*sin(theta) + b/2]; 
        end
    end
    %---Ellipses---
    if Flag == 7
        for j = 1:120
            theta = 2*j*pi/120;
            PointLoc(j,1:2) = [Incsize(1,1)*cos(theta), Incsize(1,2)*sin(theta)];
        end
    end
    %---Kidneys---
    if Flag == 8
        R1 =  Incsize(1,1); R2 = Incsize(1,2); K1 = Incsize(1,3); a = Incsize(1,4);
        for j = 1:120
            theta = (j-1)*pi/60;
            PointLoc(j,1:2) = [R1*cos(theta) + K1*exp(-a*cos(theta) - a), R2*sin(theta)];
        end
    end
    %---Stars---
    if Flag == 9
        Incs = 2*sin(18*pi/180)*Incsize(1,1); 
        d = Incs/2/tan(18*pi/180) - Incsize(1,2)/sin(18*pi/180) + Incs/2/tan(36*pi/180);
        e = Incs/2/sin(36*pi/180) + Incsize(1,2)/cos(36*pi/180);
        for j = 1:73
            theta = (j + 81 - 1)*pi/90;
            PointLoc(j,1:2) = [Incsize(1,2)*cos(theta) - d*cos(54*pi/180), Incsize(1,2)*sin(theta) - d*sin(54*pi/180)]; 
            %
            theta = (j - 63 - 1)*pi/90;
            PointLoc(j + 109,1:2) = [Incsize(1,2)*cos(theta) + d*cos(54*pi/180), Incsize(1,2)*sin(theta) - d*sin(54*pi/180)]; 
            %
            theta = (j - 27 - 1)*pi/90;
            PointLoc(j + 218,1:2) = [Incsize(1,2)*cos(theta) + d*cos(18*pi/180), Incsize(1,2)*sin(theta) + d*sin(18*pi/180)]; 
            %
            theta = (j + 9 - 1)*pi/90;
            PointLoc(j + 327,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) + d]; 
            %
            theta = (j + 45 - 1)*pi/90;
            PointLoc(j + 436,1:2) = [Incsize(1,2)*cos(theta) - d*cos(18*pi/180), Incsize(1,2)*sin(theta) + d*sin(18*pi/180)]; 
        end
        for j = 1:37
            theta = (63 - j - 1)*pi/90;
            PointLoc(j + 73,1:2) = [Incsize(1,2)*cos(theta), Incsize(1,2)*sin(theta) - e]; 
            %
            theta = (99 - j - 1)*pi/90;
            PointLoc(j + 182,1:2) = [Incsize(1,2)*cos(theta) + e*cos(18*pi/180), Incsize(1,2)*sin(theta) - e*sin(18*pi/180)]; 
            %
            theta = (135 - j - 1)*pi/90;
            PointLoc(j + 291,1:2) = [Incsize(1,2)*cos(theta) + e*cos(54*pi/180), Incsize(1,2)*sin(theta) + e*sin(54*pi/180)]; 
            %
            theta = (171 - j - 1)*pi/90;
            PointLoc(j + 400,1:2) = [Incsize(1,2)*cos(theta) - e*cos(54*pi/180), Incsize(1,2)*sin(theta) + e*sin(54*pi/180)]; 
            %
            theta = (27 - j - 1)*pi/90;
            PointLoc(j + 509,1:2) = [Incsize(1,2)*cos(theta) - e*cos(18*pi/180), Incsize(1,2)*sin(theta) - e*sin(18*pi/180)]; 
        end
    end
    %------------
    PointLoc(Numpt,1:2) = PointLoc(1,1:2);
end