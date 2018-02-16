# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午7:03'

import matplotlib.pyplot as plt
import numpy as np

#第一个y坐标
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1
fig, ax1 = plt.subplots()

#第二个y坐标
ax2 = ax1.twinx()   #对ax1调用twinx()方法，生成如同镜面效果后的ax2

ax1.plot(x, y1, 'g-')
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')

ax2.plot(x, y2, 'b--')
ax2.set_ylabel('Y2 data', color='b',)

plt.show()

