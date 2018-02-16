#-*-coding:utf-8-*-
from snownlp import sentiment
sentiment.train('neg.txt', 'pos.txt') #消极文本，积极文本      txt格式按行存储     记得修改txt编码为utf8，另存为时有选项
sentiment.save('my_sentiment.marshal')  #生成训练文件

#训练好后把生成的文件放到下面文件夹里
#D:\Python2.7\Lib\site-packages\snownlp\sentiment
#然后修改D:\Python2.7\Lib\site-packages\snownlp\sentiment\__init__.py里的data_path



#mac里：
#/Library/Python/2.7/site-packages/snownlp/sentiment
















