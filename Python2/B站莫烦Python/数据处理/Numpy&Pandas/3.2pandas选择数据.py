# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午6:22'

import pandas as pd
import numpy as np

dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print df['A'],'\n',df.A

print df[0:3],'\n',df['20180102':'20180104']

#通过label(标签)选择：loc
print df.loc['20180102']

print df.loc[:,['A','B']]

print df.loc['20180102',['A','B']]

#通过position(数字)选择：iloc
print df.iloc[3]    #第3行
print df.iloc[3,1]
print df.iloc[3:5,1:3]
print df.iloc[[1,3,5],1:3]

#混合上述两种筛选：ix
print df.ix[:3,['A','B']]

#条件筛选
print df[df.A>8]

