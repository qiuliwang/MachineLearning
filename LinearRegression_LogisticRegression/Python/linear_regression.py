# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Sat Feb 20 20:02:08 2016
Logistic Regression
@author: liudiwei
"""
import numpy as np


class LinearRegression():
    
    def __init__(self):
        self._alpha = None

    #定义一个sigmoid函数
    def _sigmoid(self, fx):
        return 1.0/(1 + np.exp(-fx))

    #alpha为步长（学习率）；maxCycles最大迭代次数
    def _gradDescent(self, featData, labelData, alpha, maxCycles):
        dataMat = np.mat(featData)                      #size: m*n
        x, y = np.shape(dataMat)
        labelMat = np.mat(labelData).transpose()        #size: m*1
        m, n = np.shape(dataMat)
        weigh = np.ones((n, 1)) 
        flag = weigh
        for i in range(maxCycles):
            hx = dataMat * weigh
            error = labelMat - hx       #size:m*1
            #print error[1]
            try:
                weigh = weigh + alpha * dataMat.transpose() * error/m#根据误差修改回归系数
            except Exception as e:
                print e
                break
        return weigh

    #使用梯度下降方法训练模型，如果使用其它的寻参方法，此处可以做相应修改
    def fit(self, train_x, train_y, alpha=0.01, maxCycles=100):
        return self._gradDescent(train_x, train_y, alpha, maxCycles)