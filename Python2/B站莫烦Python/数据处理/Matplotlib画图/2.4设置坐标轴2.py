# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午3:34'

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

#设置x轴和y轴范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#设置坐标轴标签
plt.xlabel('I am x')
plt.ylabel('I am y')

#坐标轴小标
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$really\ bad$',r'$bad\ \ \alpha$','normal','good','really good'])   # $...$好看的字体  \alpha:α

#移动坐标轴的位置
ax=plt.gca()
#去掉上边框和右边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#用边框代替坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#挪动
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()










