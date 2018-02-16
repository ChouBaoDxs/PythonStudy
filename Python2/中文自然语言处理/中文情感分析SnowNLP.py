# -*- coding: UTF-8 -*-
#https://github.com/isnowfy/snownlp

#详细原理解析
#http://blog.csdn.net/yyxyyx10/article/details/62428238

# SnowNLP库：
# words：分词
# tags：关键词
# sentiments：情感度
# pinyin：拼音
# keywords(limit)：关键词
# summary：关键句子
# sentences：语序
# tf：tf值
# idf：idf值

from snownlp import SnowNLP

s = SnowNLP(u'多只创业板ETF自11月23日大盘调整以来出现明显净申购')
#分词
for e in s.words:
    print e,
print ''
#积极的概率
print s.sentiments

s = SnowNLP(u'多只创业板ETF现净申购 部分机构布局中小盘成长股')
#分词
for e in s.words:
    print e,
print ''
#积极的概率
print s.sentiments

s = SnowNLP(u'公募逆市狂买1000亿 股基平均仓位超91%')
#分词
for e in s.words:
    print e,
print ''
#积极的概率
print s.sentiments

s=SnowNLP(u" ")
print "空字符串的情感"+str(s.sentiments)


# from snownlp import sentiment
# 关于训练
# 现在提供训练的包括分词，词性标注，情感分析，而且都提供了我用来训练的原始文件 以分词为例 分词在snownlp/seg目录下
# from snownlp import seg
# seg.train('data.txt')
# seg.save('seg.marshal')
# from snownlp import tag
# tag.train('199801.txt')
# tag.save('tag.marshal')
# from snownlp import sentiment
# sentiment.train('neg.txt', 'pos.txt') #消极文本，积极文本      txt格式按行存储
# sentiment.save('sentiment.marshal')
# 这样训练好的文件就存储为seg.marshal了，之后修改snownlp/seg/__init__.py里的data_path指向刚训练好的文件即可



text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
s = SnowNLP(text)
print '关键词:',
print s.keywords(3)	# [u'语言', u'自然', u'计算机']
for i in s.keywords(3):
    print i
print '摘要:',
print s.summary(3)
for i in s.summary(3):
    print i
print '句子:',
print s.sentences
for i in s.sentences:
    print i

s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
print s.tf
print s.idf
print s.sim([u'文章'])
print s.sim([u'这个'])