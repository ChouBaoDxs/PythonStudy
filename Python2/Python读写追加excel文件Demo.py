# -*- coding: UTF-8 -*-
'''
三个工具包

python操作excel的三个工具包如下，注意，只能操作.xls，不能操作.xlsx。

xlrd: 对excel进行读相关操作
xlwt: 对excel进行写相关操作
xlutils: 对excel读写操作的整合
这三个工具包都可以直接使用pip进行下载：

sudo pip install xlrd
sudo pip install xlwt
sudo pip install xlutils

xlwt的缺陷：

xlwt只能创建一个全新的excel文件,然后对这个文件进行写入内容以及保存。但是大多数情况下我们希望的是读入一个excel文件，然后进行修改或追加，这个时候就需要xlutils了。
'''
#xlutils的简单使用
#下面的demo是给一个excel文件追加内容：

#coding:utf-8

from xlrd import open_workbook
from xlutils.copy import copy

rexcel = open_workbook("grade.xls") # 用wlrd提供的方法读取一个excel文件
rows = rexcel.sheets()[0].nrows # 用wlrd提供的方法获得现在已有的行数
excel = copy(rexcel) # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
table = excel.get_sheet(0) # 用xlwt对象的方法获得要操作的sheet
values = ["1", "2", "3"]
row = rows
for value in values:
    table.write(row, 0, value) # xlwt对象的写方法，参数分别是行、列、值
    table.write(row, 1, u"哈哈")
    table.write(row, 2, u"拉拉")
    row += 1
excel.save("grade.xls") # xlwt对象的保存方法，这时便覆盖掉了原来的excel
















