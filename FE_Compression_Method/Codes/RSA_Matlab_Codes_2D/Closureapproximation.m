function ForientA = Closureapproximation(a)
%-----------------------------------------------------------------------------------------------------------  
    [TransM, EigV] = TransMatrix(a);

    PN = EigV(1,1);

    alpha = FindCoefficients(PN); 

    a1 = [1 0; 0 0];
    dim = 1;
    A1 = Closureapproximation1(a1,dim);
    
    a2 = [0.5 0; 0 0.5];
    dim = 2;
    A2 = Closureapproximation1(a2,dim);
    
    A = alpha(1,1)*A1 + alpha(1,2)*A2;
    
    ForientA = zeros(2,2,2,2);
    for i = 1:2
        for j = 1:2
            for k = 1:2
                for l = 1:2
                    for i1 = 1:2
                        for j1 = 1:2
                            for k1 = 1:2
                                for l1 = 1:2
                                    ForientA(i,j,k,l) = ForientA(i,j,k,l) + TransM(i,i1)*TransM(j,j1)*TransM(k,k1)*TransM(l,l1)*A(i1,j1,k1,l1);
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    
end
