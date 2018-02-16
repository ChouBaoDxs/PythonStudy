# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/16 下午9:56'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Series
data=pd.Series(np.random.randn(100),index=np.arange(100))
data=data.cumsum()

data.plot() # plt.plot(x=,y=)
plt.show()

#DataFrame
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD"))
data=data.cumsum()
print data.head()
data.plot()
plt.show()

#plot methods:'bar','hist','box','kde','area','scatter','hexbin'
# plt.scatter(x=,y=)  #分布点
# ax=data.plot.scatter(x='A',y='B',collor='DarkBlue',label='Class 1')       
ax=data.plot.scatter(x='A',y='B',c='b',label='Class 1')
# data.plot.scatter(x='A',y='C',collor='DarkGreen',label='Class 2',ax=ax)
data.plot.scatter(x='A',y='C',c='g',label='Class 2',ax=ax)
plt.show()







