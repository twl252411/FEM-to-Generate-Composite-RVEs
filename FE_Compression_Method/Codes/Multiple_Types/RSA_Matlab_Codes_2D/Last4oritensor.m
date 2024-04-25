function LastA = Last4oritensor(Orientation,AreaMat,Area,NumInc)
    LastA = zeros(2,2,2,2);
    for ii = 1:NumInc   
        if mod(ii,9) == 0
            id = 9;
        else
            id = mod(ii,9);
        end
        for i =1:2
            for j =1:2
                for k =1:2
                    for l =1:2                        
                        LastA(i,j,k,l) = LastA(i,j,k,l) + AreaMat(1,id)/Area*Orientation(ii,i)*Orientation(ii,j)*Orientation(ii,k)*Orientation(ii,l);
                    end
                end
            end
        end
    end
end