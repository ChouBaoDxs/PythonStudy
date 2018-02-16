# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午2:29'

import numpy as np

a=np.array([2,3,4])
print a.dtype,a

#指定数据类型
a=np.array([2,3,4],dtype=np.int32)
print a.dtype,a

a=np.array([2,3,4],dtype=np.float64)
print a.dtype,a

#创建多维
a=np.array([
    [2,3,4],
    [5,6,7]
])
print a

#创建全0矩阵
a=np.zeros((2,3))
print a

#创建全1矩阵
a=np.ones((2,3),dtype=np.int16)
print a

#创建空矩阵,其实是非常接近于0的数字
a=np.empty((2,3))
print a

#给定一个范围，生成连续矩阵
a=np.arange(0,20,2) #起始，终止，步长
print a
#改变矩阵形状
a=a.reshape(2,5)
print a

#创建线段型数据
a=np.linspace(0,20,5)  #起始，终止，分段数
print a