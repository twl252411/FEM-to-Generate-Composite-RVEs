function [EigB, EigV] = TransMatrix(Ori_a)
%
    [EigB1, EigV1] = eig(Ori_a);
    EA = [1 0; 0 1];
    EigB = EigB1;
    EigV = EigV1;
%
    if EigV(1,1) < EigV(2,2)
        Temp = EigV(1,1);
        EigV(1,1) = EigV(2,2);
        EigV(2,2) = Temp;

        Temp = EigB(:,1);
        EigB(:,1) = EigB(:,2);
        EigB(:,2) = Temp;
    end

    TransM = zeros(2,2);
    for i = 1:2
        for j = 1:2
            TransM(i,j) = dot(EA(:,i),EigB(:,j)');
        end
    end
end
    













