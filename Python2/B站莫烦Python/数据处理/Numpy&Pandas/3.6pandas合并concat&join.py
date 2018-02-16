# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午8:58'

import pandas as pd
import numpy as np

#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

#这些矩阵的列索引都是一样的，所以上下合并
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True) #axis=0垂直合并  axis=1水平合并   ignore_index=True：忽略原本的行索引
# print res

#join:['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print df1
print df2
res=pd.concat([df1,df2])    #由于列索引和行索引都不同，所以会用nan填补空缺值，这里的join默认为'outer'
# print res
res=pd.concat([df1,df2],join='inner',ignore_index=True)    #join='inner'会裁剪空缺值
# print res

#join_axes
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])   #水平合并，按照df1的行索引合并
print res
