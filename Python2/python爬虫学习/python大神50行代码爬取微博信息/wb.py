# -*- coding: UTF-8 -*-

from lxml import html   #解析器，比bs4快
import requests
import json
import re

# uid:1748075785  *
# luicode:20000174
# featurecode:20000320
# type:uid    *
# value:1748075785    *
# containerid:1005051748075785    *

class Tool:
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
    def replace(cls,x):
        x=re.sub(cls.removeImg,'',x)
        x=re.sub(cls.removeAddr,'',x)
        x=re.sub(cls.replaceLine,'',x)
        x=re.sub(cls.removeTag,'',x)
        return x.strip()#切除两头的空格

class Weibo(object):
    def get_weibo(self,id,page):
        '''
        获取指定博主的所有微博
        :param id: 微博博主id
        :param page: 页数
        :return: list_cards
        '''
        url='https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}'.format(id,id,id,page)
        response=requests.get(url)
        ob_json=json.loads(response.text)
        # print ob_json
        list_crads=ob_json.get('cards')
        return list_crads

    def get_comments(self,id,page):
        '''
        获取某条微博的热门评论
        :param id:
        :param page:
        :return:
        '''
        url='https://m.weibo.cn/api/comments/show?id={}&page={}'.format(id,page)
        response=requests.get(url)
        ob_json=json.loads(response.text)
        list_comments=ob_json.get('hot_data')
        return list_comments

    def main(self,uid,page):
        list_cards=self.get_weibo(uid,page)
        for card in list_cards:
            if card.get('card_type')==9:    #不等于9的话，就是广告或其他的东西
                id=card.get('mblog').get('id')  #获取某一条微博的id
                text=card.get('mblog').get('text')  #获取某一条微博的内容

                text=Tool.replace(text)

                print '***'
                print u'微博:'+text+'\n'

                list_comments=weibo.get_comments(id,1)  #热门评论可能为空
                if list_comments is None:continue

                count_hotcomments=1
                for comment in list_comments:
                    created_at=comment.get('created_at')    #获取时间
                    like_counts=comment.get('like_counts')  #获取点赞数
                    text=comment.get('text')
                    tree=html.fromstring(text)
                    text=tree.xpath('string(.)')    #用string函数过滤多余的标签
                    name_user=comment.get('user').get('screen_name')#获取评论的用户名
                    source=comment.get('source')    #手机型号
                    if source=='':
                        source=u'未知'
                    print str(count_hotcomments),':**用户名:',name_user,'**发表时间:',created_at,'**点赞数:',like_counts,'**手机型号:',source
                    print text+'\n'
                    count_hotcomments+=1
                print '==============='

if __name__=='__main__':
    weibo=Weibo()
    weibo.main(1748075785,1)
















