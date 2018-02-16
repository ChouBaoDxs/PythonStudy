# -*- coding: UTF-8 -*-
import pandas as pd
import re

class DATA:
    def __init__(self):

        path='/Users/choubao/Desktop/财经/云财经概念20171118/关联企业信息0.xls'
        path = unicode(path, 'utf8')
        table_name='Sheet 1'
        data=pd.read_excel(path,table_name)
        # print type(data)
        # print data
        # print (data.iloc[1, 0])
        # x=data.iloc[1, 0]
        # print type(x)

        # 输出点东西看看
        # print data.columns #输出列名
        shaixuan=data[data[u'概念名称'].isin([u'3D电视'])]
        print shaixuan

        for i in range(1,30):   #一共有0-29   30个excel    0已经在上面加载过了
            path2 = '/Users/choubao/Desktop/财经/云财经概念20171118/关联企业信息{}.xls'.format(i)
            path2 = unicode(path2, 'utf8')
            table_name2 = 'Sheet 1'
            data2 = pd.read_excel(path2, table_name2)

            #若不指定ignore_index参数，则会把添加的数据的index保留下来，
            # ignore_index=Ture则会对所有的行重新自动建立索引。
            data=data.append(data2,ignore_index=True)
        # print data

        # print "*****"   #表格里是：  南极电商（002127） 所以下面这样是不行的
        # shaixuan=data[data[u'公司名称'].isin([u'南极电商'])]
        # print shaixuan

        print "*****"   #查找公司名称
        print data[data[u'公司名称'].str.contains(u'康得新')]
        print type(data[data[u'公司名称'].str.contains(u'康得新')])

if __name__=='__main__':
    test=DATA()












