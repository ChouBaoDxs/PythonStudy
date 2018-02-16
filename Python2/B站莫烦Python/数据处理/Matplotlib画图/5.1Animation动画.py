# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午7:20'

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()

#数据是一个0~2π内的正弦曲线
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

# 构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧：
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,
# 构造开始帧函数init：
def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)
plt.show()

#将动画以mp4格式保存下来，但首先要保证已经安装了ffmpeg 或者mencoder， 更多信息参考http://matplotlib.org/api/animation_api.html
# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
