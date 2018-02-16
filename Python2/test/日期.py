# -*- coding: UTF-8 -*-
import time

t=time.time()

print t

l=time.localtime(t)

print l

t=time.strftime('%Y-%m-%d %H:%M:%S',l)
print type(t)
print t


t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print type(t)
print t

H=time.strftime('%H',time.localtime(time.time()))
print type(H)
print H
if H in ['8','20']:
    print '现在启动爬虫'




