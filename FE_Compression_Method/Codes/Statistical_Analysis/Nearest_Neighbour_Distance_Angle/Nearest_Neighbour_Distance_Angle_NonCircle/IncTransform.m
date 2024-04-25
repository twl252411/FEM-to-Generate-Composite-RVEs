function Point2 = IncTransform(theta, center, Point1)
    %
    theta = theta*pi/180;
    %
    R = [cos(theta), -sin(theta); sin(theta), cos(theta)];
    %
    Point2 = center + (R*Point1')';
    %
end