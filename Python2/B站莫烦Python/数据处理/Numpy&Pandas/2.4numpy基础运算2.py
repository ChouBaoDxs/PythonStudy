# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午3:03'

import numpy as np

A=np.arange(2,14).reshape(3,4)
print A

#求最小值、最大值的索引
print np.argmin(A)
print np.argmax(A)

#求平均值
print np.mean(A)
print A.mean()
print np.average(A)

#求中位数
print np.median(A)

#累加
print np.cumsum(A)

#累差
print np.diff(A)

#找到非0的数的位置
print np.nonzero(A)

#排序:每行各自排序
print np.sort(A)

#转置
print np.transpose(A)
print A.T

#修剪矩阵
print np.clip(A,5,9)    #<5的数都变成5，大于9的数都变成9，其余的保留原样