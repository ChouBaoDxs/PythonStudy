# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

#创建
s1=np.array([1,2,3,4])
s2=np.array([5,6,7,8])
df=pd.DataFrame([s1,s2])
print df

#创建
s1=pd.Series(np.array([1,2,3,4]))
s2=pd.Series(np.array([5,6,7,8]))
df=pd.DataFrame([s1,s2])
print df

#创建
s1=pd.Series(np.array([1,2,3,4]))
s2=pd.Series(np.array([5,6,7,8]))
df=pd.DataFrame({"a":s1,"b":s2});
print df

#添加一列
s3=pd.Series(np.array([9,10,11,'未公布']))
print s3
df[u'第3列']=s3
print df








