# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午8:04'

import pandas as pd
import numpy as np

dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

print df.dropna(axis=0,how='any')   #直接将出现nan数据的行/列舍弃
#参数how={'any','all'}：出现任一一个nan，全部为nan   默认是any
print df.dropna(axis=1)   #直接将出现nan数据的行/列舍弃

print df.fillna(value=0)   #把nan填为0

print df.isnull()   #返回是否缺失数据的True和Flase矩阵
print np.any(df.isnull())==True #出现一个nan就会返回True











