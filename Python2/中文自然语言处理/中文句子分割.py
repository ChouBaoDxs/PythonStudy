# -*- coding: UTF-8 -*-
import re

#中文句子分割方法1
def cut_sentences(sentence):
     if not isinstance(sentence, unicode):
          sentence = unicode(sentence)
     puns = frozenset(u'。！？')
     tmp = []
     for ch in sentence:
          tmp.append(ch)
          if puns.__contains__(ch):
               yield ''.join(tmp)
               tmp = []
     yield ''.join(tmp)  #yield返回一个迭代器

s = u'计算机评价效果，需要给定参考摘要作为标准答案，通过制定一些规则来给生产的摘要打分。目前使用最广泛的是ROUGH系统(Recall-Oriented Understudy for Gisting Evaluation),基本思想是将待审的摘要和参考摘要的n元组共现统计量作为评价作为评价依据，然后通过一系列标准进行打分。包括(ROUGH-N, ROUGH-L, ROUGH-W，ROUGH-S和ROUGH-SU)几个类型。 通俗地将就是通过一些定量化的指标来描述待审摘要和参考文摘之间的相似性，维度考虑比较多，在一定程度上可以很好地评价Extracive产生的摘要'
for i in cut_sentences(s):
     print(i)

#re模块的split方法:通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数。
print re.split('\W+', 'Words, words, words.')
print re.split('\W+', 'Words, words, words.', 1)
print re.split('(\W+)', 'Words, words, words.')
print re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

#中文句子分割方法2
pattern=re.compile('[，。？！；,.?!;]')
# print [u'，。？！；,.?!;']
pattern=re.compile(u'[\uff0c\u3002\uff1f\uff01\uff1b,.?!;]')
pattern=re.compile(u'[\uff0c\u3002\uff1f\uff01\uff1b]')
result=re.split(pattern,s)
for e in result:
     print e
