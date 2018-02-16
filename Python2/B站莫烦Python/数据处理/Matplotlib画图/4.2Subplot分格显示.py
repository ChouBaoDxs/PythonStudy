# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午6:46'

import matplotlib.pyplot as plt

#subplot2grid
plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)   #colspan:列跨度    rowspan:行跨度
ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

plt.show()

#gridspec
plt.figure()

import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3, 3)

ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

plt.show()

#subplots   python2.7+matplotlib1.3.1效果不如Anaconda3
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])
plt.tight_layout()
plt.show()