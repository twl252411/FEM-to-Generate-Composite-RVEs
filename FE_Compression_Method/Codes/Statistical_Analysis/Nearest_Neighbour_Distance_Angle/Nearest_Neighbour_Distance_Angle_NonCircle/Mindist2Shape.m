function mindist = Mindist2Shape(Shape1, Shape2)
    %
    numpt1 = size(Shape1, 1); numpt2 = size(Shape2, 1); mindist = 200.0;
    %
    for i = 1:numpt1
        for j = 1:numpt2
            if norm(Shape1(i, :) - Shape2(j, :)) < mindist
                mindist = norm(Shape1(i, :) - Shape2(j, :));
            end
        end
    end
    %
end