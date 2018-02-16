# -*- coding:utf-8 -*-

#下面两句是为了去掉指令集警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import numpy as np

#创建数据
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

#开始创建tensorflow结构*********************
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0)) #之所以开头大写，是因为它可能是个矩阵
biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases

#计算误差  y:判别值  y_data:真实值    loss:均方误差
loss=tf.reduce_mean(tf.square(y-y_data))    #预测值和真实值差别

#利用优化器反向传递误差，使用的误差传递方法是梯度下降法
optimizer = tf.train.GradientDescentOptimizer(0.5)  #优化器  0.5:学习效率
train = optimizer.minimize(loss)

# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好
#结束创建tensorflow结构*********************

sess=tf.Session()
sess.run(init)  #激活

for step in range(201): #200步
    sess.run(train)
    if step % 20 == 0:
        #每20步打印训练结果:Weights是向量，无法直接输出，只能通过sess.run输出
        print(step, sess.run(Weights), sess.run(biases))