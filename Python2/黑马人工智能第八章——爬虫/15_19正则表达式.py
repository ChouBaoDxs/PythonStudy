# -*- coding: UTF-8 -*-

# n=re.compile(‘\d’)	#将正则表达式编译成一个Pattern规则对象
# n.match()——从起始位置开始往后查找，返回第一个符合规则的，仅一个
# n.search()——从任意位置开始往后查找，返回第一个符合规则的，仅一个
# n.findall()——匹配所有的，返回列表
# n.finditer()——匹配所有的，返回的是一个迭代器，基本没用
# n.split()——分割字符串，返回列表
# n.sub()——替换

# match(str,begin,end)    str:要查找的字符串,begin:查找的起始位置,end:查找的结束位置
# search(str,begin,end)
# findall(str,begin,end)

import re
print 'match()'
#                                       match
pattern=re.compile(r'\d+')
m=pattern.match('aaa123bbb456')
print m
m=pattern.match('aaa123bbb456',3,5)
print m.group()

pattern=re.compile(r'([a-z]+) ([a-z]+)',re.I)    #re.S表示全部匹配   re.I忽略大小写
m=pattern.match('Hello world hello Python')
print m.group(0)  #0表示打印所有子串
print m.group(1)
print m.group(2)
print m.span(1)
print m.span(2)

print '\nsearch()'
#                                       search
pattern=re.compile(r'\d+')
m=pattern.search(r'aaa123bbb456')
print m.group()
m=pattern.search(r'aaa123bbb456',2,5)
print m.group()
print m.span()

m=pattern.search('hello 123456 789')
print m.group()
print m.span()

print '\nfindall()'
#                                       findall
pattern=re.compile(r'\d+')  #+：1个或多个
m=pattern.findall('hello 123456 789')
print m

pattern=re.compile(r'\d?')  #?：0个或1个
m=pattern.findall('hello 123456 789')
print m

pattern=re.compile(r'\d*')  #*：0个或多个
m=pattern.findall('hello 123456 789')
print m

pattern=re.compile(r'\d+')  #+：1个或多个
m=pattern.findall('aaa123bbb456',1,10)
print m
for i in m:
    print i

print 'finditer()'    #返回的是迭代器
m=pattern.finditer('aaa123bbb456')
for i in m:
    print i.group()

print '\nsub()'
#                                       sub替换
pattern=re.compile(r'(\w+) (\w+)')      #\w:匹配字母数字及下划线
str='hello 123,hello 456'
m=pattern.sub('hello world',str)
print m

m=pattern.sub(r'\1 \2',str)
print m
m=pattern.sub(r'\2 \1',str)
print m

pattern=re.compile(r'\d+')
str='abc123abc456'
m=pattern.sub(r'mm',str)
print m


