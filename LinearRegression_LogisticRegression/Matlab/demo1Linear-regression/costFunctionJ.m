%定义了一个带有3个参数的损失函数，
%X表示特征值（训练集向量）即样本矩阵
%y表示标签
%theta表示我们选取的函数的系数
function J = costFunctionJ(X,y,theta)
%求出我们样本的数量
m=size(X,1);
%计算出我们的预测值
predictions=X*theta;
%examples
%求解预测值和实际值得平方差
sqrErrors = (predictions-y).^2;
J = (1/(2*m))*sum(sqrErrors);