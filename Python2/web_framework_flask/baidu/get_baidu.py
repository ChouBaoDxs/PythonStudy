# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/5 下午2:41'

import urllib2

def getHtml(wd):
    req=urllib2.Request('https://www.baidu.com/s?wd=%s' %wd)
    req.add_header('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    html=urllib2.urlopen(req).read()
    return html

if __name__=='__main__':
    print getHtml('python')





