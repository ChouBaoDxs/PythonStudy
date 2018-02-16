# -*- encoding:utf-8 -*-

#http://www.jianshu.com/p/2052d21a704c

import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False

    # text = open("wordcloud.txt","rb").read()

    text = open("santi.txt","rb").read()
    text=text.decode('GBK')

    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "Trump.jpg"))

    wc = WordCloud(font_path='simsun.ttc',  #字体
            background_color="white", max_words=30, mask=trump_coloring,
            max_font_size=40, random_state=42)

    # generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
