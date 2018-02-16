# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午4:00'

import pandas as pd
import numpy as np

s=pd.Series([1,3,6,np.nan,44,1])
print s

dates=pd.date_range('20180101',periods=6)
print dates

#指明索引为日期，列名为A B C D，而不是0 1 2 3...
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print df

#混合型数据
df2=pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo',
})
print df2
print df2.dtypes  #列的数据类型

print df2.index     #列索引
print df2.columns   #行索引
print df2.values    #值

#描述一个DataFrame：求和、平均、中位数、最大、最小，会忽略非数值列
print df2.describe()

#DataFrame也可以转置
# df3=df2.T
# print df3

#按列索引或行索引对数据进行排序
print df2.sort_index(axis=0,ascending=False)    #ascending=False:倒序

#按某列的值进行排序
print df2.sort_values(by='E')