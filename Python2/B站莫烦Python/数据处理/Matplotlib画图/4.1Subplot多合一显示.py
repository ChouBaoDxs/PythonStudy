# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午6:41'

import matplotlib.pyplot as plt

plt.figure()
#均匀图中图
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,2])

plt.subplot(223)    #2,2,3简写成223也可以
plt.plot([0,1],[0,3])

plt.subplot(224)
plt.plot([0,1],[0,4])
plt.show()

plt.figure()
#不均匀图中图
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(235)
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])
plt.show()