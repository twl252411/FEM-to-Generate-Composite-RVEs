function alpha = FindCoefficients(PN)
    %
    P1 = [1,0]; P2 = [0.5,0.5];
    L0 = norm(P1 - P2);
    L1 = norm(PN - P2);
    L2 = norm(PN - P1);
    %
	alpha = zeros(1,2); 
	alpha(1,1) = L1/L0;
	alpha(1,2) = L2/L0;
		
end	
	