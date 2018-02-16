# -*- coding: UTF-8 -*-

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2) #使用的核心数，默认是全部的核心数
    res = pool.map(job, range(10))
    print(res)

    #apply_async只能传1个值
    res = pool.apply_async(job, (2,))
    print(res.get())

    #apply_async想要传多个值就只能使用迭代
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()
















