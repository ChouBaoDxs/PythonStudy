# -*- coding: UTF-8 -*-

import pandas as pd

path = 'test.xlsx'
path = unicode(path, 'utf8')
table_name = '工作表1'
table_name = '正则表达式'
table_name = unicode(table_name, 'utf8')
df = pd.read_excel(path, table_name)
print df
print '几种输出DataFrame列名的方式:'
print '1',
print df.columns
print '2',
# print df.columns.values #<type 'numpy.ndarray'>
# print type(df.columns.values)
print list(df.columns.values)
print '3',
print [column for column in df]
print '4',
print list(df)
print '5',
print df.columns.tolist()
print '6',
print list(df.columns)

# df.columns.values 的方法速度最快，特别是 用 tolist() 转换为list的方式。
column_name_list = df.columns.values.tolist()

# 输出第0列中含有'瑞安'字样的数据
print '测试:',
print column_name_list
# print column_name_list[0]
print '********'
print df[df[column_name_list[0]].str.contains(u'瑞安')]
print '********'


# 把nan的地方都填为"None",方便我们自己操作
df = df.fillna("None")

# 把DataFrame转化为list
import numpy as np

data_array = np.array(df)  # 首先使用np.array()函数把DataFrame转化为np.ndarray()
data_list = data_array.tolist()  # 再利用tolist()函数把np.ndarray()转为list
print data_list
print type(data_list)
print u"输出'瑞安':" + data_list[0][0]

print type(data_list[0][4])
print data_list[0][4]
print np.nan

print '测试:'
for e in data_list:
    for i in e:
        if i == "None":
            continue
        print i

df=pd.DataFrame()
print type(df)

'''
这一段我们通过逆转矩阵，把pandas自动识别到的所谓列标题（实际是数据第一行）插入回原数据的第一行
'''
data = pd.read_excel('test.xlsx',unicode('无列名', 'utf8'))
data_T = data.T
data_T.insert(0, '00', data.columns)
data = data_T.T
# 重新设置列标题
data.columns = ['概念名称', '股票名称', '关联原因','关联度']
print data