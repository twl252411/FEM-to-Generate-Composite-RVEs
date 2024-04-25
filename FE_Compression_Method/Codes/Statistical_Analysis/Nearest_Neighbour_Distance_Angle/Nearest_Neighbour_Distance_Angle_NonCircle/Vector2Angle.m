function oriangle = Vector2Angle(orientation)
    %
    oriangle = zeros(size(orientation,1),1);
    for i = 1:size(orientation,1)
        Xv = orientation(i,1); 
        Yv = orientation(i,2); 
    %    
        if Yv >= 0
           oriangle(i,1) = acos(Xv)/pi*180;
        end
        if Yv < 0
            oriangle(i,1) = 360 - acos(Xv)/pi*180;
        end
        if Xv == 0 &&  Yv > 0
            oriangle(i,1) = 90;
        end
        if Xv == 0 &&  Yv < 0
            oriangle(i,1) = 270;
        end  
    end
end