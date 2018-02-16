# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午2:49'

import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)

print a,b
c=a-b   #减法
print c

c=b**2  #平方
print c

c=np.sin(a) #sin
print c

print b
print b<3
print b==3

#矩阵
a=np.array([
    [1,1],
    [0,1]
])
b=np.array([
    [0,1],
    [2,3]
])
#逐个相乘
c=a*b
print c
#矩阵乘法
c_dot=np.dot(a,b)
c_dot_2=a.dot(b)
print c_dot
print c_dot_2

#求最大值，最小值，和
c=np.random.random((2,4))
print c
print np.sum(c,axis=1)    #axis=1：求每行
print np.min(c,axis=0)    #axis=0：求每列
print np.max(c,axis=1)

