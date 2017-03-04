function [jVal,gradient] = costFunction(theta)
  x = [-3;-2;-1;0;1;2;3];%%样本的x值
  y = [0.01;0.05;0.3;0.45;0.8;1.1;0.99];%%样本的y值
  m = size(x,1);%%样本的数量
  hypothesis = h_func(x,theta);%%根据我们的假设求出的y值
  jVal = -sum(log(hypothesis+0.01).*y+(1-y).*log(1-hypothesis+0.01))/m;%%计算损失函数
  gradient(1)=sum(hypothesis-y)/m;%%求偏倒
  gradient(2) = sum((hypothesis-y).*x)/m;%%求骗倒
 end