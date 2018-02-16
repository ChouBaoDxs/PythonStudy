# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/5 下午1:53'

from flask import Flask
from flask import render_template   #基于jinja2模板引擎
from flask import request

from get_baidu import getHtml

app=Flask(__name__)

#flask的路由实现方式：装饰器——不改变用法的情况下增加方法功能
@app.route('/') #指定路由
def index():
    # return 'Hello flask!'
    return render_template('index.html')

@app.route('/s')
def search():
    # return 'Hi flask!'
    if request.method=='GET':
        wd=request.args.get('wd')
        # wd=request.args['wd'] #这样取可能会出错
        html=getHtml(wd)
        return html

if __name__=='__main__':
    # app.run() #默认http://127.0.0.1:5000/
    # app.run(host='127.0.0.1',port=5001,debug=True)  #debug=True:有代码更新会自动重启
    app.run(host='127.0.0.1',port=5001)
    #DEBUG模式下flask开多一个线程来监视项目的变化。
    #如果想要避免加载两次，应该设置app.run(debug=True, use_reloader=False)