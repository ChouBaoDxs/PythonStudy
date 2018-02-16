# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午3:51'

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()

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

#label:给图像设置名字
l1,=plt.plot(x,y2,label='up')
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')

#显示图例标签
# plt.legend()  #默认为空也可以

#下面这句要在高版本matplotlib上有效
# plt.legend(handles=[l1,l2,],labels=['upup','downdown'],loc='best')

plt.legend([l1,l2],['upup','downdown'],loc='best') #loc=['best','upper right','upper left']

# loc:
# 'best'         : 0, (only implemented for axes legends)(自适应方式)
# 'upper right'  : 1,
# 'upper left'   : 2,
# 'lower left'   : 3,
# 'lower right'  : 4,
# 'right'        : 5,
# 'center left'  : 6,
# 'center right' : 7,
# 'lower center' : 8,
# 'upper center' : 9,
# 'center'       : 10,

plt.show()














