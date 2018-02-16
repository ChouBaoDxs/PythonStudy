# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午7:42'

import threading

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()

    print threading.active_count()  #输出当前线程数
    print threading.enumerate() #输出是哪几个线程
    print threading.current_thread()    #输出当前线程


if __name__=='__main__':
    main()
