# -*- coding: UTF-8 -*-     #Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
                            #解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
print "Hello, Python!"
print "你好，世界"

print 'hello';print 'runoob';   #Python 可以同一行显示多条语句，方法是用分号 ; 分开

#多行语句：Python语句中一般以新行作为为语句的结束符。但是我们可以使用斜杠（\）将一行的语句分为多行显示：
total = 1 + \
        2 + \
        3

#语句中包含 [], {} 或 () 括号就不需要使用多行连接符：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

#Python 引号：Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
#其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

#Print 输出：
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号：
x="a"
y="b"
# 换行输出
print x
print y
# 不换行输出
print x,
print y,
# 不换行输出
print x,y

str = 'Hello World!'
#字符串：从左到右索引默认 0 开始，从右到左索引默认 -1 开始
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[:-1]  # 输出字符串中的最后一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[:-3]
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

#列表用[]
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

#元组用()          元组不可以更新元素，相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

#dictionary：类似Objective-C的dictionary，是由key和value组成的
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

#成员运算符 in和not in
a = 1
list = [1, 2, 3, 4, 5];

if (a in list):
        print "1 - 变量 a 在给定的列表中 list 中"
else:
        print "1 - 变量 a 不在给定的列表中 list 中"

#身份运算符 is和is not
a = 20
b = 20

if (a is b):
        print "1 - a 和 b 有相同的标识"
else:
        print "1 - a 和 b 没有相同的标识"

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。


#爬虫********************************************************************
# urllib2下载网页方法1：最简洁方法
# import urllib2
# #直接请求
# response=urllib2.urlopen('http://www.baidu.com')
# #获取状态码，如果是200，表示获取成功
# print response.getcode()
# #读取内容
# cont=response.read()

# urllib2下载网页方法2：添加data、http header
# url、data、header->urllib2.Request->urllib2.urlopen(request)
# import urllib2
# #创建Request对象
# url='http://www.baidu.com'
# request=urllib2.Request(url)
# #添加数据
# request.add_data('a','1')
# #添加http的header
# request.add_header('User-Agent','Mozilla/5.0')
# #发送请求获取数据
# response=urllib2.urlopen(request)

# urllib2下载网页方法3：添加特殊情景的处理器
# HTTPCookieProcessor、ProxyHandler、HTTPSHandler、HTTPRedirectHandler->opener=urllib2.build_opener(handler)->urllib2.install_opener(opener)->response=urllib2.urlopen(url)  response=urllib2.urlopen(request)
# import urllib2,cookielib
# #创建cookie容器
# cj=cookielib.CookieJar()
# #创建一个opener
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# #给urllib2安装opener
# urllib2.install_opener(opener)
# #使用带有cookie的urllib2访问网页
# response=urllib2.urlopen("http://www.baidu.com/")

