# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:04:30 2016

@author: liudiwei
"""

from linear_regression import LinearRegression
import matplotlib.pyplot as plt

#每行数据以\t隔开，最后一列为类标号
def loadDataSet(datafile):
    featData = []; labelDate = []
    with open(datafile, 'r') as fr_file:
        for eachline in fr_file:
            oneline = eachline.split(',')
            #add data
            tempArr = []
            for i in range(len(oneline)-1):
                tempArr.append(float(oneline[i]))
            featData.append(tempArr)
            #add label
            labelDate.append(float(oneline[-1].strip()))
    return featData, labelDate
def main():
    trainfile = r"data/ex1data1.txt"
    train_X, train_y = loadDataSet(trainfile)
    clf = LinearRegression()
    weigh = clf.fit(train_X, train_y, alpha=0.01, maxCycles=500)
    Fig = plt.figure(figsize=(8,4))                      # Create a `figure' instance
    Ax = Fig.add_subplot(111)               # Create a `axes' instance in the figure
    Ax.plot(train_X, train_y, 'o')                 # Create a Line2D instance in the axes
    #Ax.plot(a1,a2)
    a1 = [0, 1]
    a2 = [0, 1 * weigh]
    b1 = [0, 25]
    b2 = [0, 25 * weigh]
    Ax.plot(a1, a2, b1, b2)
    Fig.savefig("test.pdf")
#主函数
if __name__=="__main__":
    main()