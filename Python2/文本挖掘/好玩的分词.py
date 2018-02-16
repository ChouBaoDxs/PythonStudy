# -*- coding: UTF-8 -*-

#http://www.cnblogs.com/jiayongji/p/7119065.html

import jieba
import time
jieba.initialize()  #手动初始化jieba分词词典
time.sleep(1)

s = u'我想去北京故宫博物院参观和闲逛。'

cut = jieba.cut(s)
# print cut
print '精确模式-----------------------------'
print ','.join(cut)
print '全模式------------------------------'
print ','.join(jieba.cut(s,cut_all = True))
print '搜索引擎模式-------------------------'
print ','.join(jieba.cut_for_search(s))
print '获取词性----------------------------'
import jieba.posseg as psg
# print [(x.word,x.flag) for x in psg.cut(s)]
for x in psg.cut(s):
    print x.word+" "+x.flag+",",
print '\n只获取名词--------------------------'
# print [(x.word,x.flag) for x in psg.cut(s) if x.flag.startswith('n')]
for x in psg.cut(s):
    if x.flag.startswith('n'):print x.word+" "+x.flag+",",

print ''
#并行分词
# 开启并行分词模式，参数为并发执行的进程数
jieba.enable_parallel(5)

santi_text = open('./santi.txt').read()
print len(santi_text)
santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 2]

# 关闭并行分词模式
jieba.disable_parallel()

#获取出现频率Top n的词:还是以上面的三体全集文本为例，假如想要获取分词结果中出现频率前20的词列表，可以这样获取：
from collections import Counter
c = Counter(santi_words).most_common(20)
print type(c)
for each in c:
    print each[0]+u''+str(each[1])+',',
print ''
print c



