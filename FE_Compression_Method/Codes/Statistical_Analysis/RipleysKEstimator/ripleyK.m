function [K,L] = ripleyK(dataXY,xK,box,method)
% KFUNCTION calculates Ripley's K function
% 
% OUTPUT
%  K: vector K containing values of Ripley's K function of points (spatial events) dataXY calculated for the distances (h-values) xK
%
%  L: L-function (variance stabilized Ripley K function)
%       For homogeneous data, the L(h) function has expected value of h and its variance is constant in h
%
%  For more info on K- and L-functions, see e.g. http://www.colorado.edu/geography/class_homepages/geog_4023_s11/Lecture12_PointPat1.pdf
%
% INPUT
%  dataXY - N-by-2 vector where N is number of datapoints. Each row
%       corresponds to x and y coordinates of each datapoint
%
%  xK - corresponds to the distances where K function should be computed.
%       K is the same size as xK...
%
%  box - rectangular boundary of the data: box = [xlim1, xlim2, ylim1, ylim2]
%
%  method - switch between edge correction. If method=0, no edge correction
%       is applied. If method=1, datapoint is used for estimation of K(h) only if
%       it is at least h units away from the box

% the code is mainly of Ondrej Mandula (github aludnam)
% https://github.com/aludnam/MATLAB/blob/master/PatternAnalysis/kfunction.m 
% (maybe based on
% http://www.colorado.edu/geography/class_homepages/geog_4023_s07/labs/lab10/RipleysK.m)
% 
% with minor changes by Theodore Alexandrov (github theodev), EMBL, 2014-2015


if nargin<4 method=1; end

[N,k] = size(dataXY);

if k~=2 error('dataXY must have two columns'); end

rbox = min([ dataXY(:,1)'-box(1);
    box(2)-dataXY(:,1)';
    dataXY(:,2)'-box(3);
    box(4)-dataXY(:,2)']);

% rbox is the nearest distance of each datapoint to the box
DIST = squareform(pdist(dataXY,'euclidean'));
DIST = sort(DIST);

K = zeros(size(xK));
Nk = length(K);
    
if method==1 % edge correction...
%     wb = waitbar(0,'Computing Ripley''s K-function...');
    for k=1:Nk
%         waitbar(k/Nk,wb);
        I = find(rbox>xK(k));
        if ~isempty(I)
            K(k) = sum(sum(DIST(2:end,I)<xK(k)))/length(I);
        end
    end
%     close (wb);
elseif method==0 % no correction
    for k=1:Nk
        K(k) = sum(sum(DIST(2:end,:)<xK(k)))/N;
    end
end
% fprintf ('\b'); fprintf ('\b'); fprintf ('\b'); fprintf ('\b');
% fprintf ('100%%\n');

lambda = N/((box(2)-box(1))*(box(4)-box(3)));
K = K/lambda;

L=sqrt(K/pi)-xK;