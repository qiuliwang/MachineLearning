function [ y ] = sigmoid( x )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
y=x;
for i=1:length(x)
    y(i)=1/(1+exp(-x(i)));
end
end

