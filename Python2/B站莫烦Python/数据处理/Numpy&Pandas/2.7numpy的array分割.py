# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午3:35'

import numpy as np

A=np.arange(12).reshape((3,4))
print A

print np.split(A,2,axis=1)  #按列分割，分成2等份

print np.array_split(A,3,axis=1)    #不等分分割

print np.vsplit(A,3)    #垂直分割，分成3等份

print np.hsplit(A,2)    #水平分割，分成2等份








