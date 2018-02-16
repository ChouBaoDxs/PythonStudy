# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]

#加入历史数据
# year=[1800,1850,1900]+year
# pop=[1.0,1.262,1.650]+pop

#折线图
# plt.plot(year,pop)
#填充区域
plt.fill_between(year,pop,0,color='green')

#轴标签
plt.xlabel('Year')
plt.ylabel('Population')
#标题
plt.title('World Population Projections')
#在Y轴上标出刻度
#plt.yticks([0,2,4,6,8,10])
#加上刻度2
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])
plt.show()

#散点图
plt.scatter(year,pop)
plt.show()

#直方图
values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,bins=3)
plt.show()


#真的和matlab太像了！！！真的和matlab太像了！！！真的和matlab太像了！！！真的和matlab太像了！！！















