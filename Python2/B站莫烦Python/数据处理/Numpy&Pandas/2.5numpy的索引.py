# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午3:14'

import numpy as np

A=np.arange(3,15)
print A
print A[3]

A=A.reshape(3,4)
print A[2]
print A[2][2]
print A[2,2]
print A[2,:]
print A[2,1:3]

for row in A:   #for循环默认迭代行
    print row

#想要迭代列，只需要迭代转置后的A就行
for column in A.T:
    print column

print A.flatten()   #使矩阵变平
for item in A.flat:
    print item