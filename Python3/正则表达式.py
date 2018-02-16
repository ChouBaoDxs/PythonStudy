# -*- coding: UTF-8 -*-
import re
str='I love you'
#search()方法用于在字符串中搜索正则表达式模式第一次出现的位置
a=re.search(r'love',str)
print(a)
print(str.find('love'))

a=re.search(r'.',str)  #.能匹配除了换行符以外的任何的字符       \s\S可以匹配任何字符
print(a)

a=re.search(r'\.',str+'.')  #加\可以消除特殊字符的作用
print(a)

a=re.search(r'\d',str+'1')  #加\d匹配数字
print(a)
a=re.search(r'\d\d\d',str+'123')  #加\d匹配数字
print(a)

#用[]创建字符类:匹配字符类中任何一个字符就算匹配成功
a=re.search(r'[aeiou]',str)
print(a)
a=re.search(r'[aeiouAEIOU]',str)
print(a)
#a-z:匹配小写的a到z
a=re.search(r'[a-z]',str)
print(a)
#2-9:匹配2到9
a=re.search(r'[2-9]',str+'3')
print(a)
#限定匹配的次数{}
a=re.search(r'ab{3}c','abbbc')
print(a)
#给定匹配的次数范围
a=re.search(r'ab{3,6}c','abbbbc')
print(a)
#匹配0-255的三位数
a=re.search(r'[01]\d\d| 2[0-4]\d|25[0-5]','188')
print(a)
#匹配0-255的任意数
a=re.search(r'[01]\d\d| 2[0-4]\d|25[0-5]|\d\d|\d','18')
print(a)
#匹配ip地址
a=re.search(r'(([01]\d\d| 2[0-4]\d|25[0-5]|\d\d|\d)\.){3}([01]\d\d| 2[0-4]\d|25[0-5]|\d\d|\d)','192.169.1.1')
print(a)
#^：脱字符，表示它后面跟的东西必须是字符串的开头，下面这样的匹配不出来      如果设置了re.MULTILINE标志，也匹配换行之后的位置
a=re.search(r'^abc','233abc')
print(a)
#$：结束字符，下面的就是以abc结尾的，可以找到                           如果设置了re.MULTILINE标志，也匹配换行之前的位置
a=re.search(r'abc$','233abc')
print(a)
#\：的另一个用法,\1——代表第1个子组   \2——代表第2个子组
a=re.search(r'(abc)\1','abcabc')    #r'(abc)\1' == r'abcabc'
print(a)
a=re.search(r'(abc)(ABC)\1\2','abcABCabcABC')
print(a)
#\060：代表八进制的数字0     \141：八进制的a      八进制：\+0开头的三位数，或者三位数
#[.]=\.     []字符类会让特殊符号作用消失 但\仍然是转移符


#re.findall：找到所有匹配的字符串
print(re.findall(r'[a-z]|[A-Z]',str))
#^在[]表示取反   ^必须在开头，如果放在其他地方就代表它自己^
print(re.findall(r'[^a-z]',str))
#{M,N}：代表重复的次数
print(re.search(r'abc{3}','abcccc'))
print(re.search(r'(abc){3}','abcabcabc'))
print(re.search(r'(abc){1,5}','abcabcabcabc'))
#*：等价于{0,}      任意次
#+：等价于{1,}      1次或多次
#?：等价于{0,1}     0次或1次
#*? +? ??：表示非贪婪的，使用* + ?会尽可能多地匹配字符串(即贪婪的)，比如下面的例子
print(re.search(r'abc+','abcccc'))  #匹配abcccc
print(re.search(r'abc+?','abcccc')) #匹配abc

#默认情况下：\A==^   \Z==$    设置了re.MULTILINE标志对\A和\Z无效

#\b：匹配单词边界，单词背定义为字母数字或下划线
print(re.findall(r'\blove\b','love.com (love) love_com'))   #love_com是整个单词，无法匹配
#\B：与\b相反，匹配非单词边界
print(re.findall(r'\Blove\B','love.com (love) _love_com'))

#\w	匹配字母数字及下划线，空格没办法
print(re.findall(r'\w',str+' 123_ '))

#编译正则表达式：模式对象
p=re.compile(r'[A-Z]')
print(type(p))
print(p.search(str))
print(p.findall(str))

#正则表达式的编译标志
'''
ASCII,A：使得转义字符，如\w,\b,\s,\d只能匹配ASCII字符
DOTALL,S：使得.匹配任何符号，包括换行符
IGNORECASE,I：匹配的时候不区分大小写
LOCALE,M：支持当前的语言(区域)设置
NULTILINE,M：多行匹配，影响^和$
VERBOSE,X(for'extended')：启用详细的正则表达式
'''
