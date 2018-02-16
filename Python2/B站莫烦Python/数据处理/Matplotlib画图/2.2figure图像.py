# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午3:30'

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(figsize=(8,5))   #指定size
plt.plot(x,y1)
plt.show()

plt.figure(num=3)   #指定序号为3
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=10.0,linestyle='--')
plt.show()



