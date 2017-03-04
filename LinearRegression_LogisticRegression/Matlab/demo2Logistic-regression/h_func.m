function [res] = h_func(X,theta)
  temp = theta(1)+theta(2)*X;%%先计算出假设函数的值
  res = 1./(1+exp(-temp));%% 计算出逻辑模型sigmoid函数值
  end