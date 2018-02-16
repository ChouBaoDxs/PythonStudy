# -*- coding: UTF-8 -*-

import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
booksheet=workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
DATA=(
    ('学号','姓名','年龄','性别','成绩'),
      ('1001','A','11','男','12'),
      ('1002','B','12','女','22'),
      ('1003','C','13','女','32'),
      ('1004','D','14','男','52'),
)
# enumerate()是python的内置函数
# enumerate在字典上是枚举、列举的意思
# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# enumerate多用于在for循环中得到计数
for i,row in enumerate(DATA):
    for j,col in enumerate(row):
        booksheet.write(i,j,col)
workbook.save('grade.xls')

'''
上述方法有些累赘，利用enumerate()会更加直接和优美：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item
>>>
0 这
1 是
2 一个
3 测试

enumerate还可以接收第二个参数，用于指定索引起始值，如：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print index, item
>>>
1 这
2 是
3 一个
4 测试

补充
如果要统计文件的行数，可以这样写：
count = len(open(filepath, 'r').readlines())

这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
可以利用enumerate()：
count = 0
for index, line in enumerate(open(filepath,'r'))： 
    count += 1
'''












