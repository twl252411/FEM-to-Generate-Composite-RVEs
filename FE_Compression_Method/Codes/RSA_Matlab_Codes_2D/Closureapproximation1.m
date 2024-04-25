function ForientA = Closureapproximation1(a,dim)
%-----------------------------------------------------------------------------------------------------------       
     if dim == 1
        Aq = zeros(2,2,2,2);
        for i = 1:2
            for j = 1:2
                for k = 1:2
                    for l = 1:2
                        Aq(i,j,k,l) = a(i,j)*a(k,l);
                    end
                end
            end
        end
        ForientA = Aq;
     end
%-----------------------------------------------------------------------------------------------------------   
    if dim ~= 1 && dim == 2   
        alpha = -1/24.0; beta = 1/6;   
        I2 = zeros(2,2); I2(1,1) = 1.0; I2(2,2) = 1.0; 
        
        Al = zeros(2,2,2,2);
        Temp1 = zeros(2,2,2,2);
        Temp2 = zeros(2,2,2,2);
        Temp3 = zeros(2,2,2,2);
        Temp4 = zeros(2,2,2,2);
        Temp41 = zeros(2,2,2,2);
        Temp42 = zeros(2,2,2,2);
        
        Ta = a + I2;
        for i = 1:2
            for j = 1:2
                for k = 1:2
                    for l = 1:2
                        Temp1(i,j,k,l) = alpha*I2(i,j)*I2(k,l);
                        Temp2(i,j,k,l) = 2*(alpha - beta)*1/2*(I2(i,k)*I2(j,l) + I2(i,l)*I2(j,k));
                        Temp3(i,j,k,l) = beta*(I2(i,j)*a(k,l) + a(i,j)*I2(k,l));
                        Temp41(i,j,k,l) = 1/2*(Ta(i,k)*Ta(j,l) + Ta(i,l)*Ta(j,k));
                        Temp42(i,j,k,l) = 1/2*(a(i,k)*a(j,l) + a(i,l)*a(j,k));                        
                        Temp4(i,j,k,l) = 2*beta*(Temp41(i,j,k,l) - Temp42(i,j,k,l));
                        Al(i,j,k,l) = Temp1(i,j,k,l) + Temp2(i,j,k,l) + Temp3(i,j,k,l) + Temp4(i,j,k,l);                                    
                    end
                end
            end
        end   
        ForientA = Al;
    end
%    
end
