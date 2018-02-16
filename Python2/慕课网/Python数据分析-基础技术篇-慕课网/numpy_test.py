# -*- coding: UTF-8 -*-

import numpy as np


def main():
    lst = [[1, 3, 5], [2, 4, 6]]  # 可以有多种类型
    print (type(lst))
    np_lst = np.array(lst)  # 只能有一种类型
    print (type(np_lst))
    # 给定类型:bool,int,int8/16/32/64/128,uint8/16/32/64/128,float,float16/32/64,complex64/128
    np_lst = np.array(lst, dtype=np.float)
    print (np_lst.shape)
    print (np_lst.ndim)  # 维度
    print (np_lst.dtype)
    print (np_lst.itemsize)  # 每个元素所占空间的大小
    print (np_lst.size)
    # Some Arrays
    print (np.zeros([2, 4]))  # 0矩阵
    print (np.ones([3, 5]))  # 1矩阵
    print (np.random.rand(2, 4))  # 随机矩阵
    print (np.random.rand())  # 打印一个随机数
    print (np.random.randint(1, 10, 3))  # 打印3个1-10之间的随机数
    print (np.random.randn(2, 4))  # 标准正态分布的随机数
    print (np.random.choice([10, 20, 30]))  # 从给定的数中随机选择一个
    print (np.random.beta(1, 10, 5))  # 打印5个beta分布
    # Array Opes
    print (np.arange(1, 11))  # 等差数列
    print (np.arange(1, 11).reshape([2, 5]))  # 等差数列,排成2行5列
    lst = (np.arange(1, 11).reshape([2, -1]))  # 效果和上面一样
    print (np.exp(lst))
    print (np.exp2(lst))
    print (np.sqrt(lst))
    print (np.sin(lst))
    print (np.log(lst))

    lst = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                    ])
    print (lst.sum())
    print (lst.sum(axis=0))
    print (lst.sum(axis=1))

    print '******************'
    print (lst.max(axis=1))
    print (lst.min(axis=0))

    print '******************'
    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print (lst1 + lst2)
    print (lst1 * lst2)
    print '******************'
    # 矩阵相乘(.乘)
    print (np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
    # 连接矩阵
    print (np.concatenate((lst1, lst2), axis=0))
    # 按列连接矩阵
    print (np.vstack((lst1, lst2)))
    # 按行连接矩阵
    print (np.hstack((lst1, lst2)))
    # 拆分矩阵
    print (np.split(lst1, 2))
    # 拷贝矩阵
    lst3 = np.copy(lst1)
    print lst3

    print '******************'
    # liner 线性代数
    from numpy.linalg import *
    print (np.eye(3))  # 打印大小为3的单位矩阵
    lst = np.array([[1, 2],
                    [3, 4]
                    ])
    print (inv(lst))  # 逆矩阵
    print (lst.transpose())  # 转置矩阵
    print (det(lst))  # 计算行列式结果
    print (eig(lst))  # 特征值,特征向量
    y = np.array([[5.], [7.]])
    # 解方程:这里是二元一次方程组
    print (solve(lst, y))

    print '******************'
    # Others 其他
    print (np.fft.fft(np.array([1, 1, 1, 1, 1, 1])))  # FFT（Fast Fourier Transformation）是离散傅氏变换（DFT）的快速算法。即为快速傅氏变换。
    print (np.corrcoef([1, 0, 1], [0, 2, 1]))  # 相关系数
    #print (np.polyld([2, 1, 3]))  # 根据参数产生一个多项式,报错啊

if __name__ == '__main__':
    main()
