# -*- coding: UTF-8 -*-
import re
class Cut_Label:
    '''
    去除html多余标签的工具类
    '''
                                #这里是代表1到7个的空格
    removeImg=re.compile('<img.*?>| {1,7}|&nbsp;')  #去除img标签
    removeAddr=re.compile('<a.*?>|</a>')            #去除超链接 a标签
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')#把换行变成\n
    #去除所有标签
    removeTag=re.compile('<.*?>')

    @classmethod    #装饰器,表示这是一个类方法
    def cut(cls,x):
        x=re.sub(cls.removeImg,'',x)
        x=re.sub(cls.removeAddr,'',x)
        x=re.sub(cls.replaceLine,'',x)
        x=re.sub(cls.removeTag,'',x)
        return x.strip()#切除两头的空格