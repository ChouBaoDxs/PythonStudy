# -*- coding: UTF-8 -*-

import jieba
import jieba.posseg as pseg
import jieba.analyse

str1 = "我来到北京清华大学"
str2 = 'python的正则表达式是好用的'
str3 = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"

seg_list = jieba.cut(str1,cut_all = True)   ##全模式
result = pseg.cut(str1)                     ##词性标注，标注句子分词后每个词的词性
result2 = jieba.cut(str2)                   ##默认是精准模式

##关键词提取，参数setence对应str1为待提取的文本,topK对应2为返回几个TF/IDF权重最大的关键词，默认值为20
result3 =  jieba.analyse.extract_tags(str1,2)

result4 = jieba.cut_for_search(str3)        ##搜索引擎模式

print '分割---------------------------------------------'
print "/".join(seg_list)

print '词性标注------------------------------------------'
for w in  result:
    print w.word, "/", w.flag, ",",
print ''

print '精准模式------------------------------------------'
for t in result2:
    print t,'/'
print ''

print '关键词提取----------------------------------------'
for s in result3:
    print u'关键词:'+s
print '搜索引擎模式--------------------------------------'
print ",".join(result4)










