# -*- coding: UTF-8 -*-

#NLP--- 初识文本挖掘
#http://www.jianshu.com/p/3d767cb5db59

def fenci():
    # 2.2 分词
    # 2.2.1 分词模式
    import jieba
    testSentence = "利用python进行数据分析"
    print(u"1.精准模式分词结果："+"/".join(jieba.cut(testSentence,cut_all=False)))
    print(u"2.全模式分词结果："+"/".join(jieba.cut(testSentence,cut_all=True)))
    print(u"3.搜索引擎模式分词结果："+"/".join(jieba.cut_for_search(testSentence)))
    print(u"4.默认（精准模式）分词结果："+"/".join(jieba.cut(testSentence)))

    # 2.2.2 查看词性
    import jieba.posseg
    testSentence = "利用python进行数据分析"
    words = jieba.posseg.cut(testSentence)
    for item in words:
        print(item.word+"----"+item.flag)

def custom_dict():
    # 2.3 添加自定义词典
    # 2.3.1 词典加载
    import jieba.posseg
    #词典加载
    testSentence2="简书书院是一个很好的交流平台"
    # testSentence2="南洋股份002212SZ是一个好的上市公司"
    # testSentence2="电池锂"
    print("+---------+---------+---------+---------+---------+---------+---------+----")
    print("1.加载词典前分词结果：")
    # print([item for item in jieba.posseg.cut(testSentence2)])
    for item in jieba.posseg.cut(testSentence2):
        print item,
    print("\n+---------+---------+---------+---------+---------+---------+---------+----")
    jieba.load_userdict("/Users/choubao/Desktop/dict_2.txt")
    # print("2.加载词典后分词结果：")
    # jieba.add_word('简书书院',3,'n')
    # jieba.add_word('南洋股份',3,'n')
    # jieba.add_word('002212SZ',3,'bh')
    # jieba.add_word('锂',10,'xjs')
    print("2.增加词句后分词结果：")
    # print([item for item in jieba.posseg.cut(testSentence2)])
    for item in jieba.posseg.cut(testSentence2):
        print item,
    print("\n+---------+---------+---------+---------+---------+---------+---------+----")

    # 2.3.2 调整词典
    # 只能调高词频，不能调低词频
    # add_word(word, freq=None, tag=None)
    # suggest_freq(segment, tune=True)
    # 只能降低词频，不能调高词频
    # del_word(word)
    # suggest_freq(("segmentPart1", "segmentPart2"), True)

    # （1）调高词频
    import jieba
    print(u"1.原始分词结果：" + "/".join(jieba.cut("数据分析与数据挖掘的应用", HMM=False)))
    jieba.add_word("的应用")
    print(u"2.使用add_word(word, freq=None, tag=None)结果：" + "/".join(jieba.cut("数据分析与数据挖掘的应用", HMM=False)))
    jieba.suggest_freq("的应用", tune=True)
    print(u"3.使用suggest_freq(segment, tune=True)结果：" + "/".join(jieba.cut("数据分析与数据挖掘的应用", HMM=False)))

    # （2）降低词频
    import jieba
    jieba.suggest_freq(("中", "将"), True)
    print(u"使用suggest_freq(('segmentPart1','segmentPart2'),True)分词结果：" + "/".join(jieba.cut("在简书中将尽力呈现优质内容", HMM=False)))

def analyse_fenci():
    # 2.4 分词分析:进一步,我们需要对文本信息进行相关分析，如返回词语所在位置、返回关键词等等。
    # 2.4.1返回词语所在位置
    import jieba.analyse
    print("1.采取精准模式结果：")
    # print([item for item in jieba.tokenize(u"数据分析与数据挖掘的应用")])
    for item in jieba.tokenize(u"数据分析与数据挖掘的应用"):
        print item[0],item[1],item[2]
    print("-------------------")
    print("2.采取搜索模式结果：")
    # print([item for item in jieba.tokenize("数据分析与数据挖掘的应用", mode="search")])
    for item in jieba.tokenize(u"数据分析与数据挖掘的应用", mode="search"):
        print item[0],item[1],item[2]

    # 2.4.2提取文本中的关键词
    print '提取文本中的关键词:'                                          #其结果是结合文中出现的词频与字典中的词频进行排序
    import jieba.analyse
    # print(jieba.analyse.extract_tags("我喜欢广州小蛮腰", 3))
    # print(jieba.analyse.extract_tags("我喜欢广州广州小蛮腰", 3))
    # print(jieba.analyse.extract_tags("我喜欢广州广州广州小蛮腰", 3))
    for item in jieba.analyse.extract_tags("我喜欢广州小蛮腰", 3):
        print item+' ',
    print ''
    for item in jieba.analyse.extract_tags("我喜欢广州广州小蛮腰", 3):
        print item+' ',
    print ''
    for item in jieba.analyse.extract_tags("我喜欢广州广州广州小蛮腰", 3):
        print item+' ',
    print ''

def text_similarity():
    '''
    利用gensim做TF-IDF主题模型
    '''
    from gensim import corpora, models, similarities
    import jieba
    from collections import defaultdict
    # 1.导入句子
    sentence1 = "我喜欢吃番薯"
    sentence2 = "番薯是个好东西"
    sentence3 = "利用python进行文本挖掘"
    # 2.分词
    data1 = " ".join(jieba.cut(sentence1))
    data2 = " ".join(jieba.cut(sentence2))
    data3 = " ".join(jieba.cut(sentence3))
    # 3.转换格式："词语1 词语2 词语3 … 词语n"
    texts = [list(data1), list(data2), list(data3)]
    # for each in texts:
    #     for i in each:
    #         print i
    # 4.基于文本建立词典
    dictionary = corpora.Dictionary(texts)
    featureNum = len(dictionary.token2id.keys())  # 提取词典特征数
    dictionary.save("./dictionary.txt")  # 保存语料库
    # 5.基于词典建立新的语料库
    corpus = [dictionary.doc2bow(text) for text in texts]
    # 6.TF-IDF处理
    tfidf = models.TfidfModel(corpus)

    # 输出每个句子每个词语的tfidf值
    # corpus_tfidf = tfidf[corpus]
    # for doc in corpus_tfidf:
    #     print(doc)

    # 7.加载对比句子并整理其格式
    query = "吃东西"
    data4 = jieba.cut(query)
    data41 = ""
    for item in data4:
        data41 += item + " "
    new_doc = data41
    # 8.将对比句子转换为稀疏向量
    new_vec = dictionary.doc2bow(new_doc.split())
    # 9.计算相似性
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)
    sim = index[tfidf[new_vec]]
    for i in range(len(sim)):
        print("查询与第" + str(i + 1) + "句话的相似度为:" + str(sim[i]))

if __name__=='__main__':
    #分词
    # fenci()
    #自定义词典
    custom_dict()
    #分词分析
    # analyse_fenci()

    # 3.文本相似度
    # 3.2实战
    # 3.2.1需求:假设我们有一个搜索引擎资源库，里面包含sentence1，sentence2，sentence3三个句子，现在我们将要进行查询并按相似度进行排序返回结果。
    # 注意：官方文档中提示建立的语料库是存在内存中的一个列表格式，因此对于很大的语料库，最好还是存在硬盘上，
    # 然后依次访问文件。这样可以不用考虑语料库的大小，也避免了占用太多内存。

    # TF - IDF：是一种用于资讯检索与资讯探勘的常用加权技术。
    # （1）TF(term frequency)
    # 词频，指的是某一个给定的词语在该文档中出现的频率。计算公式为某词在一个文档中出现的次数除以所有字词在该文档中出现的次数。
    # 其中以所有字词在文档中出现的系数作为分母目的在于将词数进行归一化是为了防止偏向长的文档(不管该词语重要与否，同一个词语在长文档里可能会比短文件有更高的词数）。
    # （2）IDF（inverse document frequency）
    # 逆向文件频率，是一个词语普遍重要性的度量。计算公式为总文档数目除以包含该词语之文件的数目，再将得到的商取对数。
    # （3）计算实例
    # 词语“母牛”在某一篇总词语数为100个的文件出现了3次，该文件所在的语料库的文件总数为10, 000, 000
    # 份，并且“母牛”在其中的1, 000
    # 份文件出现过，那么“母牛”一词在该文件中的词频就是3 / 100 = 0.03，其逆向文件频率为
    # log(10, 000, 000 / 1, 000) = 4。最后的TF - IDF的分数为0
    # .03 * 4 = 0.12。
    # 参考：TF - IDF及其算法

    #有问题********************************************************************************
    # text_similarity()














