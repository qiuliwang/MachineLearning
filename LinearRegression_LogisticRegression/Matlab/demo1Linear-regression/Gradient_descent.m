 function [optTheta,functionVal,exitFlag] = Gradient_descent()
   options = optimset('GradObj','on',"MaxIter",100);
   initialTheta = zeros(2,1);%初始化theta的值
   [optheta,functionVal,exitFlag] = fminunc(@costFunction2,initialTheta,options);
 end

  
