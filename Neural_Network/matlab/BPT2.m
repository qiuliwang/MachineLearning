%BP神经网络算法----自适应阈值
clc
clear
disp('开始训练...')

tic;
data=[0 0 0;0 1 1;1 0 1;1 1 0];
n=2;%输入节点数
h=2;%隐层节点数
m=1;%输出层节点数
xlyb=[1 2 3 4];
x_xl=data(xlyb,1:2); %训练样本x_xl
x_xl=[x_xl -1*ones(length(xlyb),1)];%添加阈值项
d_xl=data(xlyb,3);%训练期望输出

%初始化相关参数
w=0.1*randn(h+1,m);%输出权矩阵
v=0.1*randn(n+1,h);%隐层权矩阵
delta_v=zeros(h,1);%隐层权矩阵修改量
delta_w=zeros(m,1);%输出层权矩阵修改量
o1=zeros(h,1);%隐层输出向量
o2=zeros(m,1);%输出层输出向量
e=0.01;%误差控制精度
M=1000; %训练次数控制
a=0.4; %学习率
E=1;%训练误差
N=0;%训练次数累计量
dv=v;%v增量
dw=w;%w增量

while N<5000 && E>e
    N=N+1;E=0;
    %对每一组样本数据(x_xl,d_xl)进行训练
    for num=1:length(d_xl)
        %隐  层输出o1
        o1=sigmoid((x_xl(num,:)*v)');
        %输出层输出o2
        o1=[o1;-1];%添加阈值项
        o2=sigmoid((o1'*w)');
        %输出层权矩阵修改量
        for i=1:m
            delta_w(i)=o2(i)*(1-o2(i))*(d_xl(num,i)-o2(i));
            %输出误差
            E=E+(d_xl(num,i)-o2(i))*(d_xl(num,i)-o2(i));
        end
        %隐藏层权矩阵修改量
        for i=1:h
            z=0;
            for j=1:m
                z=z+w(i,j)*delta_w(j);
            end
            delta_v(i)=z*o1(i)*(1-o1(i));
        end
        %修改输出权矩阵
        for j=1:h+1
            for k=1:m
                dw(j,k)=a*o1(j)*delta_w(k);
                w(j,k)=w(j,k)+dw(j,k);
            end
        end
        %修改隐层权矩阵
        for i=1:n+1
            for j=1:h
                dv(i,j)=a*x_xl(num,i)*delta_v(j);
                v(i,j)=v(i,j)+dv(i,j);
            end
        end
    end
end
disp(['训练误差E：',num2str(E)]);
disp(['训练次数N：',num2str(N)]);
disp(['BP神经网络训练时间：',num2str(toc)])

disp('Test...');
for num=1:length(xlyb)
    o1=sigmoid((x_xl(num,:)*v)');
    o1=[o1;-1];%添加阈值项
    o2=sigmoid((o1'*w)');
    disp(['期望值',num2str(d_xl(num,:),'%1.0f\t\t')]);
    disp(['预测值',num2str(o2','%5.4f\t')]);
end
disp('隐层权矩阵：v=');
disp(num2str(v));
disp(['隐层阈值1：',num2str(-v(3,1)),'阈值2：',num2str(-v(3,2))]);
disp('输出层权矩阵：w=');
disp(num2str(w));
disp(['输出层阈值：',num2str(-w(3,1))]);