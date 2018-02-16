# -*- coding: UTF-8 -*-

import numpy as np

height=[1.73,1.68,1.71,1.89,1.79]
weight=[65.4,59.2,63.6,88.4,68.7]

#weight/height **2  #list可没这么聪明

np_height=np.array(height)
np_weight=np.array(weight)

print np_weight/np_height **2

#numpy数组：元素只有一种类型  如果声明时类型不一致，会强行转变类型
#numpy的构造子集
#array[1]
#array>23    #会得到一个bool数组
#array[array>23] #会得到>23的数组

#numpy.ndarray #代表n维数组
#.shape 可以得到(行数,列数)
#np.mean() 平均数
#np.median() 中位数
#np.corrcoef() 相关性分析，参见SPSS

#大量数据的产生
# height=np.round(np.random.normal(1.75,0.20,5000),2)
# weight=np.round(np.random.normal(60.32,15,5000),2)
# np_city=np.column_stack((height,weight))









