# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午7:59'

import threading
import time
import Queue    #python2
# from queue import Queue   #python3
#使用Queue原因，Threading没有返回值

def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)   #多线程调用的函数不能用return返回值

def multithreading():
    # q =Queue()    #python3
    q =Queue.Queue()    #python2
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

    for i in range(4):  # 定义四个线程
        t = threading.Thread(target=job, args=(data[i], q))  # Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
        t.start()  # 开始线程
        threads.append(t)  # 把每个线程append到线程列表中

    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())  # q.get()按顺序从q中拿出一个值
    print(results)

if __name__=='__main__':
    multithreading()
