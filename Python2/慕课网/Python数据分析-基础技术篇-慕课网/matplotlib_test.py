# -*- coding: UTF-8 -*-

import numpy as np


def main():
    #线性图
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  #-pi到+pi，256个点，包含最后一个点
    c, s = np.cos(x), np.sin(x)  # 定义好余弦函数和正弦函数
    plt.figure(1)
    # plt.plot(x,c)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cos", alpha=0.5)
    # plt.plot(x,s)
    plt.plot(x, s, "r*", label="sin")
    plt.title("cos & sin")

    ax=plt.gca()#轴的编辑器
    ax.spines["right"].set_color("none")    #隐藏右边界
    ax.spines["top"].set_color("none")      #隐藏上边界
    ax.spines["left"].set_position(("data",0))  #把数据标在左边界上，并从0开始
    ax.spines["bottom"].set_position(("data",0))#把数据标在下边界上，并从0开始

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
               [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$',])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    #修改标签的字体
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)  #设置字号
        label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.2))

    plt.legend(loc="upper left")#显示图像说明label
    plt.grid()#设置网格线
    # plt.axis([-1,1,-0.5,1]) #设置显示范围
    plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color='green',alpha=0.25)#填充颜色：横轴，判断型变量，纵轴，判断型变量，颜色，透明度
    t=1
    plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
    #下面是标注出一个点
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),
                 textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
    plt.show()

    #散点图
    fig=plt.figure()
    fig.add_subplot(3,3,1)
    n=128
    X=np.random.normal(0,1,n)
    Y=np.random.normal(0,1,n)
    T=np.arctan2(Y,X)
    plt.axes([0.025,0.025,0.95,0.95])
    plt.scatter(X,Y,s=75,c=T,alpha=.5)
    plt.xlim(-1.5,1.5),plt.xticks([])
    plt.ylim(-1.5,1.5),plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    fig = plt.figure()
    ax=fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    ax.scatter(X, Y, s=75, c=T, alpha=.5)
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()

    #柱状图
    fig.add_subplot(332)
    n=10
    X=np.arange(n)
    Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
    Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
    plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
    plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
    for x,y in zip(X,Y1):
        plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom')
    for x,y in zip(X,Y2):
        plt.text(x+0.4,-y-0.05,'%.2f'%y,ha='center',va='top')
    #plt.show()

    #饼图
    fig.add_subplot(333)
    n=20
    Z=np.ones(n)
    Z[-1]*=2
    plt.pie(Z,explode=Z*.05,colors=['%f'%(i/float(n)) for i in range(n)],
            labels=['%.2f'%(i/float(n))for i in range(n)])
    plt.gca().set_aspect('equal')#设置成正圆型
    plt.xticks([]),plt.yticks([])

    #极坐标图polar
    fig.add_subplot(334,polar=True)
    n=20
    theta=np.arange(0.0,2*np.pi,2*np.pi/n)
    radii=10*np.random.rand(n)
    plt.polar(theta,radii)
    # plt.plot(theta,radii)

    #热图heatmap
    fig.add_subplot(335)
    from matplotlib import cm
    data=np.random.rand(3,3)
    cmap=cm.Blues
    map=plt.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)

    #3D图      2.7好像不行
    # from mpl_toolkits.mplot3d import Axes3D
    # ax=fig.add_subplot(336,projection="3d")
    # ax.scatter(1,1,3,s=100)

    #hot map
    fig.add_subplot(313)
    def f(x,y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    X,Y=np.meshgrid(x,y)
    plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.hot)

    #保存图片
    # plt.savefig("./data/fig.png")
    plt.show()


if __name__ == '__main__':
    main()
