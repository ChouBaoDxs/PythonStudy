# -*- coding: UTF-8 -*-

text = open("白色家电.xls", "r").read()
print text

for line in open("白色家电.xls"):
    print line

f = open("白色家电.txt", "r")
for line in f:
    print line
f.close()

f = open("白色家电.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    print line                 # 后面跟 ',' 将忽略换行符
    line = f.readline()
f.close()

f=open('白色家电.txt', 'r')
s=f.readlines()
print s
print type(s)
print len(s)
for each in s:
    print each
    print type(each)

print type(s[0])
print s[0]

list=s[0].split('\t')
for i in list:
    print i




