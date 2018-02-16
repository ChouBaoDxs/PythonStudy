# -*- coding:utf-8 -*-

#下面两句是为了去掉指令集警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

#创建两个矩阵
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])

#矩阵乘法
product = tf.matmul(matrix1,matrix2)

#有两种形式使用会话控制 Session
#形式1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
# [[12]]

#形式2，这种方式会自动close
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
# [[12]]
