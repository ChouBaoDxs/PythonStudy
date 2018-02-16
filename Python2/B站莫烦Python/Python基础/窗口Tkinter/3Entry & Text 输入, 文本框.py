# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午9:25'

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
# e = tk.Entry(window, show="*")    #用*代替内容显示
# e = tk.Entry(window, show="1")    #用1代替内容显示
e = tk.Entry(window)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    t.insert('end', var)

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)       #插入内容到光标所在处
b1.pack()
b2 = tk.Button(window, text='insert end',           #插入内容到文本结尾
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()

window.mainloop()