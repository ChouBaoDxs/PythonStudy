# -*- coding: UTF-8 -*-

import multiprocessing as mp
#多进程无法通过global交流数据

value=mp.Value('d',1)   #这样就可以被每一个进程读取
array=mp.Array('i',[1,2,3])    #只能是一维数组












