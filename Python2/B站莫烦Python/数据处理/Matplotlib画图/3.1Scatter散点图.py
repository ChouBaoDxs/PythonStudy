# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午5:34'

import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
T = np.arctan2(Y,X) # 每个点的颜色

#大面积的散点图
plt.scatter(X, Y, s=75, c=T, alpha=.5)

#一条线的散点图
# plt.scatter(np.arange(10),np.arange(10))

# plt.xlim(-1.5, 1.5)
plt.xticks(())  # 去掉x轴刻度
# plt.ylim(-1.5, 1.5)
plt.yticks(())  # 去掉y轴刻度

plt.show()
