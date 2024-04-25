function LastA = Last4oritensor(Orientation,NumInc)
    LastA = zeros(2,2,2,2);
    for ii = 1:NumInc       
        for i =1:2
            for j =1:2
                for k =1:2
                    for l =1:2
                        LastA(i,j,k,l) = LastA(i,j,k,l) + 1.0/NumInc*Orientation(ii,i)*Orientation(ii,j)*Orientation(ii,k)*Orientation(ii,l);
                    end
                end
            end
        end
    end
end