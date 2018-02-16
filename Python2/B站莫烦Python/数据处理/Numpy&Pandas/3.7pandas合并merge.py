# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午8:58'

import pandas as pd

#merging two df by key/keys
left=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
})

right=pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
})
# print left
# print right
res=pd.merge(left,right,on='key')   #基于key合并
print res


#consider two keys    基于两个key
left=pd.DataFrame({
    'key1':['K0','K0','K1','K2'],
    'key2':['K0','K1','K0','K1'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
})

right=pd.DataFrame({
    'key1':['K0','K1','K1','K2'],
    'key2':['K0','K0','K0','K0'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
})

res=pd.merge(left,right,on=['key1','key2'],how='inner') #how=['left','right','outer','inner']
print res
# res=pd.merge(left,right,on=['key1','key2'],how='outer')
# print res
# res=pd.merge(left,right,on=['key1','key2'],how='left')
# print res
# res=pd.merge(left,right,on=['key1','key2'],how='right')
# print res


#在合并的结果中显示合并方式  indicator=True
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

res=pd.merge(df1,df2,on='col1',how='outer',indicator=True)
print res

#自定义indicator的列名
res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
print res


#merged by index    通过index合并
left=pd.DataFrame(
    {'A':['A0','A1','A2'],
     'B':['B0','B1','B2']},
    index=['K0','K1','K2']
)

right=pd.DataFrame(
    {'C':['C0','C1','C2'],
     'D':['D0','D1','D2']},
    index=['K0','K2','K3']
)
res=pd.merge(left,right,left_index=True,right_index=True,how='inner')
print res

#handle overlapping     区分列索引名相同的情况
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
res=pd.merge(boys,girls,on='k',suffixes=['_boys','_girls'],how='inner')
print res