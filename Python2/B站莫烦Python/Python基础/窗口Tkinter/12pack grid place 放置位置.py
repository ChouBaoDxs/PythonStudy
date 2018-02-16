# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午9:34'

import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

#方式一
# tk.Label(window, text='1').pack(side='top')
# tk.Label(window, text='1').pack(side='bottom')
# tk.Label(window, text='1').pack(side='left')
# tk.Label(window, text='1').pack(side='right')

#方式二
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

#方式三
# tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()