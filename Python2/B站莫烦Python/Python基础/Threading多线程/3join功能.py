# -*- coding:utf-8 -*-
import time

__author__ = 'dxs'
__date__ = '2018/1/17 下午7:46'

import threading

def thread_job():
    print('T1 start')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish')

def T2_job():
    print 'T2 start'
    print 'T2 finish'

def main():
    added_thread=threading.Thread(target=thread_job,name='T1')
    thread2=threading.Thread(target=T2_job,name='T2')

    added_thread.start()
    thread2.start()

    added_thread.join() #等待added_thread执行完才执行后面的语句
    thread2.join()

    print 'all done'

if __name__=='__main__':
    main()

