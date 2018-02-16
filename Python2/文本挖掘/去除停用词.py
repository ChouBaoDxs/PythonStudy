# -*- coding: UTF-8 -*-

import jieba

# 去除停用词
stopwords = {}.fromkeys(['的', '包括', '等', '是'])
text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常精美，午门是紫禁城的正门。"
segs = jieba.cut(text, cut_all=False)
final = ''
for seg in segs:
    seg = seg.encode('utf-8')
    if seg not in stopwords:
        final += seg
print final
# 输出:故宫著名景点乾清宫、太和殿和午门。其中乾清宫非常精美，午门紫禁城正门。

seg_list = jieba.cut(final, cut_all=False)
print "/ ".join(seg_list)
#输出:故宫/ 著名景点/ 乾清宫/ 、/ 太和殿/ 和/ 午门/ 。/ 其中/ 乾清宫/ 非常/ 精美/ ，/ 午门/ 紫禁城/ 正门/ 。















