# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午8:58'

import pandas as pd
import numpy as np

#append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

#添加一个DataFrame
res=df1.append(df2,ignore_index=True)
print res

#添加多个DataFrame
res=df1.append([df2,df3],ignore_index=True)
print res

#添加一个Series
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)
print res