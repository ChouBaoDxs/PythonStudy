# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午8:51'

import tkinter as tk

#窗口主体框架
window = tk.Tk()
window.title('my window')
window.geometry('200x100')

#窗口内容--------------------------------------
var = tk.StringVar()    # 这是文字变量储存器
#标签
l = tk.Label(window,
    # text='OMG! this is TK!',    # 标签的文字
    textvariable=var,
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
l.pack()    # 固定窗口位置



on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空

#按钮
b = tk.Button(window,
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2,
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

window.mainloop()














