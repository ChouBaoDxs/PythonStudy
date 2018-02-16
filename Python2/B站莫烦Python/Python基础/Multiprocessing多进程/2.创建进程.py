# -*- coding: UTF-8 -*-

import multiprocessing as mp
import threading as td

def job(a,b,c):
    print '233'
    print a,b,c

if __name__=='__main__':
    # t1=td.Thread(target=job,args=(1,2,3))
    p1=mp.Process(target=job,args=(1,2,3))

    # t1.start()
    p1.start()

    # t1.join() #让主线程阻塞，等待子线程执行结束
    p1.join()   #让主线程阻塞，等待子线程执行结束












