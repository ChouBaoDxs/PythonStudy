# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午5:57'

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

#填充颜色
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

#画等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5) #8代表等高线的密集程度，这里被分为10个部分。如果是0，则图像被一分为二。

#加标签
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()