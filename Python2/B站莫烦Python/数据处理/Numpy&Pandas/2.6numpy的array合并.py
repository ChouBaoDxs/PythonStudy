# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午3:23'

import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])

#垂直合并
print np.vstack((A,B))

#水平合并
print np.hstack((A,B))

#增加维度
print A.shape
A1=A[np.newaxis,:]
print A1.shape
A2=A[:,np.newaxis]
print A2.shape
A3=A.reshape(3,1)
print A3.shape

#另一种方式合并
C=np.concatenate((A,B),axis=0)
print C




