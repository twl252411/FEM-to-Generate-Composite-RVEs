clear;
clc;
%
Points = importdata('NewCentroids.txt');
Angles = importdata('NewOriangles.txt');
NumInc = size(Points,1);
PInc = 18*2;
NumI = zeros(1,9);
for i = 1:9
    if i <= mod(NumInc - PInc, 9)
        NumI(1,i) = floor((NumInc - PInc)/9) + 4 + 1;
    else
        NumI(1,i) = floor((NumInc - PInc)/9) + 4;
    end
end
%
%---Circles---361
Incsize =4.0; Numpt1 = 361;
PointLoc1 = GeometryLoc(Incsize, Numpt1,1);
%---Lobular2s---
Incsize = 3.0; Numpt2 = 601;
PointLoc2 = GeometryLoc(Incsize, Numpt2,2);
%---Lobular3s---
Incsize = 2.25; Numpt3 = 721;
PointLoc3 = GeometryLoc(Incsize, Numpt3,3);
%---Lobular4s---
Incsize = 2.0; Numpt4 = 841;
PointLoc4 = GeometryLoc(Incsize, Numpt4,4);
%---Spolygon3s---
Incsize = [12, 1.5]; Numpt5 = 364;
PointLoc5 = GeometryLoc(Incsize, Numpt5,5);
%---Spolygon4s---
Incsize = [7.5, 1.5]; Numpt6 =365;
PointLoc6 = GeometryLoc(Incsize, Numpt6,6);
%---Ellipses---
Incsize = [6, 3]; Numpt7 =361;
PointLoc7 = GeometryLoc(Incsize, Numpt7,7);
%---Kidneys---
Incsize = [4.0, 6.0, 2.8, 4.8]; Numpt8 =361;
PointLoc8 = GeometryLoc(Incsize, Numpt8, 8);
%---Stars---
Incsize = [5.5, 1.0]; Numpt9 =1090;
PointLoc9 = GeometryLoc(Incsize, Numpt9, 9);
%
PointInc1 = zeros(Numpt1, 2*NumI(1,1));
PointInc2 = zeros(Numpt2, 2*NumI(1,2));
PointInc3 = zeros(Numpt3, 2*NumI(1,3));
PointInc4 = zeros(Numpt4, 2*NumI(1,4));
PointInc5 = zeros(Numpt5, 2*NumI(1,5));
PointInc6 = zeros(Numpt6, 2*NumI(1,6));
PointInc7 = zeros(Numpt7, 2*NumI(1,7));
PointInc8 = zeros(Numpt8, 2*NumI(1,8));
PointInc9 = zeros(Numpt9, 2*NumI(1,9));
Inum = zeros(1,9);
for i = 1:NumInc
    phi = Angles(i,1)*pi/180;
    R = [cos(phi), -sin(phi); sin(phi), cos(phi)];
    if mod(i,9) == 1 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 1 && i > NumInc - PInc
        Inum(1,1) = Inum(1,1) + 1;
        for j = 1:Numpt1
            Temp = R*(PointLoc1(j,1:2))';
            PointInc1(j,(Inum(1,1)-1)*2+1:(Inum(1,1)-1)*2+2) = Points(i,1:2) + Temp';
        end
    end
    if mod(i,9) == 2 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 2 && i > NumInc - PInc
        Inum(1,2) = Inum(1,2) + 1;
        for j = 1:Numpt2
            Temp = R*(PointLoc2(j,1:2))';
            PointInc2(j,(Inum(1,2)-1)*2+1:(Inum(1,2)-1)*2+2) = Points(i,1:2) + Temp';
        end
    end
    if mod(i,9) == 3 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 3 && i > NumInc - PInc
        Inum(1,3) = Inum(1,3) + 1;
        for j = 1:Numpt3
            Temp = R*(PointLoc3(j,1:2))';
            PointInc3(j,(Inum(1,3)-1)*2+1:(Inum(1,3)-1)*2+2) = Points(i,1:2) + Temp';
        end
    end
    if mod(i,9) == 4 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 4 && i > NumInc - PInc
        Inum(1,4) = Inum(1,4) + 1;
        for j = 1:Numpt4
            Temp = R*(PointLoc4(j,1:2))';
            PointInc4(j,(Inum(1,4)-1)*2+1:(Inum(1,4)-1)*2+2) = Points(i,1:2) + Temp';
        end
    end
     if mod(i,9) == 5 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 5 && i > NumInc - PInc
        Inum(1,5) = Inum(1,5) + 1;
        for j = 1:Numpt5
            Temp = R*(PointLoc5(j,1:2))';
            PointInc5(j,(Inum(1,5)-1)*2+1:(Inum(1,5)-1)*2+2) = Points(i,1:2) + Temp';
        end
     end
      if mod(i,9) == 6 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 6 && i > NumInc - PInc
          Inum(1,6) = Inum(1,6) + 1;
          for j = 1:Numpt6
              Temp = R*(PointLoc6(j,1:2))';
              PointInc6(j,(Inum(1,6)-1)*2+1:(Inum(1,6)-1)*2+2) = Points(i,1:2) + Temp';
          end
      end
      if mod(i,9) == 7 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 7 && i > NumInc - PInc
          Inum(1,7) = Inum(1,7) + 1;
          for j = 1:Numpt7
              Temp = R*(PointLoc7(j,1:2))';
              PointInc7(j,(Inum(1,7)-1)*2+1:(Inum(1,7)-1)*2+2) = Points(i,1:2) + Temp';
          end
      end
      if mod(i,9) == 8 && i <= NumInc - PInc || mod(i - NumInc + PInc,9) == 8 && i > NumInc - PInc
          Inum(1,8) = Inum(1,8) + 1;
          for j = 1:Numpt8
              Temp = R*(PointLoc8(j,1:2))';
              PointInc8(j,(Inum(1,8)-1)*2+1:(Inum(1,8)-1)*2+2) = Points(i,1:2) + Temp';
          end
      end
      if mod(i,9) == 0 && i <= NumInc - PInc || mod(i - NumInc + PInc, 9) == 0 && i > NumInc - PInc
          Inum(1,9) = Inum(1,9) + 1;
          for j = 1:Numpt9
              Temp = R*(PointLoc9(j,1:2))';
              PointInc9(j,(Inum(1,9)-1)*2+1:(Inum(1,9)-1)*2+2) = Points(i,1:2) + Temp';
          end
      end
end
%
writematrix(PointInc1, 'OriginPoints1.xlsx'); 
writematrix(PointInc2, 'OriginPoints2.xlsx'); 
writematrix(PointInc3, 'OriginPoints3.xlsx'); 
writematrix(PointInc4, 'OriginPoints4.xlsx'); 
writematrix(PointInc5, 'OriginPoints5.xlsx'); 
writematrix(PointInc6, 'OriginPoints6.xlsx'); 
writematrix(PointInc7, 'OriginPoints7.xlsx'); 
writematrix(PointInc8, 'OriginPoints8.xlsx'); 
writematrix(PointInc9, 'OriginPoints9.xlsx'); 
