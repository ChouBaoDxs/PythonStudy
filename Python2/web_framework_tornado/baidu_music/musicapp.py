# -*- coding: UTF-8 -*-

from tornado import web,httpserver,ioloop
from music_spider import get_music_info_by_name

#逻辑处理模块——部门
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('hello tornado')

class IndexPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class GetMusicInfoHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        #拿到需要搜索的关键字
        query=self.get_argument('query')
        print query
        #下一步要去爬取数据
        music_info=get_music_info_by_name(query)
        # print music_info[0]
        self.render('music.html',music=music_info)

#路由——分机号
application=web.Application([
    (r"/",MainPageHandler),
    (r"/index",IndexPageHandler),
    (r"/query",GetMusicInfoHandler),
])

#socket服务——前台
if __name__=='__main__':
    http_server=httpserver.HTTPServer(application)
    http_server.listen(8888)    #http://127.0.0.1:8888/query
    ioloop.IOLoop.current().start()

















