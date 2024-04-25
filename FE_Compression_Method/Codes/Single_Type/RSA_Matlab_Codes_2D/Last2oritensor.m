function LastA = Last2oritensor(Orientation,NumInc)
    LastA = zeros(2,2);
    for ii = 1:NumInc       
        for i =1:2
            for j =1:2
                  LastA(i,j) = LastA(i,j) + 1.0/NumInc*Orientation(ii,i)*Orientation(ii,j);
            end
        end
    end
end