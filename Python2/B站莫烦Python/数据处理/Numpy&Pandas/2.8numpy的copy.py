# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午3:43'

import numpy as np

a=np.arange(4)
print a
b=a
c=a
d=b

a[0]=11
print a
print b is a
print b

d[1:3]=[22,33]
print a

b=a.copy()  #deep copy深度复制：a不会和b关联起来
a[3]=44
print a,b

