# -*- coding:utf-8 -*-

# https://www.bilibili.com/watchlater/#/av18404929/p1
# pip install web.py
import web

# web.application().run()
# 上面一行代码就可以运行了
# 如何运行？ 进入项目文件夹执行：python weixin.py 端口号   #默认端口号为8080
# 停止：control+c


urls=(
    '/weixin','Weixin',
    '/dxs','Dxs',
)

class Weixin:
    def GET(self):
        # return 'Hello Weixin!'
        #业务逻辑
        i=web.input()#获取请求参数
        print i
        str=i.get('echostr')
        return str;

    def POST(self):
        # i=web.input()
        i=web.data()    #仅用于获取post数据
        print i
        return 'Hello'

if __name__=='__main__':
    web.application(urls,globals()).run()