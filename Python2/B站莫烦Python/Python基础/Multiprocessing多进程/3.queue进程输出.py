# -*- coding: UTF-8 -*-

import multiprocessing as mp
import threading as td

def job(q):
    res=0
    for i in range(1000):
        res+=i
    q.put(res)

if __name__=='__main__':

    q=mp.Queue()

    p1=mp.Process(target=job,args=(q,)) #(q,)表示其可迭代，(q)可能会报错
    p2=mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()   #让主线程阻塞，等待子线程执行结束
    p2.join()
    res1=q.get()
    res2=q.get()
    print res1+res2









