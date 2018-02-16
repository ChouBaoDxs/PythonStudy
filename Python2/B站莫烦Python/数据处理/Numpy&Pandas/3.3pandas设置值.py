# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午7:57'

import pandas as pd
import numpy as np

dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2]=1111
df.loc['20180101','B']=2222
df.A[df.A>0]=0  #仅把A列大于0的数变成0
# df[df.A>0]=0  #把A列大于0的数所在的行全都变成0
print df

#加一个空列
df['F']=np.nan
print df

#加一个序列
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))
print df







