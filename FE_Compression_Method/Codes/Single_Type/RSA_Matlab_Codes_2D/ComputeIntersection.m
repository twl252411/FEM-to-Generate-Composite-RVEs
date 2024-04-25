function [Edge, End] = ComputeIntersection(sValue, classify, F00, F10, mB)
    % The divisions are theoretically numbers in [0,1].  Numerical rounding
    % errors might cause the result to be outside the interval.  When this
    % happens, it must be that both numerator and denominator are nearly
    % zero.  The denominator is nearly zero when the segments are nearly
    % perpendicular.  The numerator is nearly zero when the P-segment is
    % nearly degenerate (mF00 = a is small).  The choice of 0.5 should not
    % cause significant accuracy problems.
    %
    % NOTE:  You can use bisection to recompute the root or even use
    % bisection to compute the root and skip the division.  This is generally
    % slower, which might be a problem for high-performance applications.
    
    Edge = zeros(2,1);
    End = zeros(2,2);

    if (classify(1,1) < 0)
        Edge(1,1) = 0; 
        End(1,1) = 0; 
        End(1,2) = F00 / mB;
        if (End(1,2) < 0 || End(1,2) > 1)
            End(1,2) = 0.5;
        end

        if (classify(2,1) == 0)
            Edge(2,1) = 3;
            End(2,1) = sValue(2,1); 
            End(2,2) = 1;
        else  % classify(2,1) > 0
            Edge(2,1) = 1;
            End(2,1) = 1; 
            End(2,2) = F10 / mB;
            if (End(2,2) < 0 || End(2,2) > 1)
                End(2,2) = 0.5;
            end
        end
    elseif (classify(1,1) == 0)
        Edge(1,1) = 2;
        End(1,1) = sValue(1,1);
        End(1,2) = 0;
        
        if (classify(2,1) < 0)
            Edge(2,1) = 0;
            End(2,1) = 0;
            End(2,2) = F00 / mB;
            if (End(2,2) < 0 || End(2,2) > 1)
                End(2,2) = 0.5;
            end
        elseif (classify(2,1) == 0)
            Edge(2,1) = 3;
            End(2,1) = sValue(2,1);
            End(2,2) = 1;
        else
            Edge(2,1) = 1;
            End(2,1) = 1;
            End(2,2) = F10 / mB;
            if (End(2,2) < 0 || End(2,2) > 1)
                End(2,2) = 0.5;
            end
        end
	else  %classify(1,1) > 0
        Edge(1,1) = 1;
        End(1,1) = 1;
        End(1,2) = F10 / mB;
        if (End(1,2) < 0 || End(1,2) > 1)
            End(1,2) = 0.5;
        end

        if (classify(2,1) == 0)
            Edge(2,1) = 3;
            End(2,1) = sValue(2,1);
            End(2,2) = 1;
        else
            Edge(2,1) = 0;
            End(2,1) = 0;
            End(2,2) = F00 / mB;
            if (End(2,2) < 0 || End(2,2) > 1)
                End(2,2) = 0.5;
            end
        end
    end
end