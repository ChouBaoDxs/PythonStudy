# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午8:48'

import pandas as pd

'''
read_csv
read_excel
read_hdf
read_sql
read_json
read_html
read_pickle #pandas专用格式
...
对应read的是to_XXX
'''

data=pd.read_csv('student.csv')
print data

data.to_pickle('student.pickle')







