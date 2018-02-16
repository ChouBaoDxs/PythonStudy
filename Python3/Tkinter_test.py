# -*- coding: UTF-8 -*-

from tkinter import *

#python的GUI编程
'''
top=tkinter.Tk()
#进入消息循环
top.mainloop()

root = tkinter.Tk()             # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = tkinter.Listbox(root)          #  创建两个列表组件
listb2 = tkinter.Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环
'''

root=Tk() #初始化Tk()
root.title("巨潮资讯网最新公告")   #设置窗口标题
root.geometry('800x800')    #设置窗口大小
root.resizable(width=True,height=True)  #设置宽可变，高可变

t = Text(root)

t.insert(1.0, '300413快乐购		分析结果：secondary	公告标题：关于股东权益变动的提示性公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, '300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告\n')
t.insert(END, 'nono')
t.pack()
root.mainloop()


#Label：Label(根对象, [属性列表])
# -*- coding: cp936 -*-
'''
root = Tk()
root.title("hello world")
root.geometry('300x200')
l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
l.pack(side=LEFT)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop()
'''

#Frame：Frame(根对象, [属性列表])       在屏幕上创建一块矩形区域,多作为容器来布局窗体
'''
root =Tk()
root.title("hello world")
root.geometry('300x200')

Label(root, text='校训', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬业', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='乐群', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)
frm.pack()
root.mainloop()
'''

#Entry：创建单行文本框
# 　　创建:lb =Entry(根对象, [属性列表])
# 　　绑定变量 var=StringVar()    lb=Entry(根对象, textvariable = var)
# 　　获取文本框中的值   var.get()
# 　　设置文本框中的值   var.set(item1)
'''
root = Tk()
root.title("hello world")
root.geometry()
var = StringVar()
e = Entry(root, textvariable=var)
var.set("hello")
# var.set("300413快乐购		分析结果：secondary	公告标题：第三届董事会第四次会议决议公告")
e.pack()
root.mainloop()
'''


#一个例子
'''
# -*- coding:cp936 -*-
from Tkinter import *

class show:
    num_info_hash = {}
    char_info_hash = {}
    num_char = {}
    char_num = {}
    def __init__(self):
        
        self.root = Tk()
        self.root.title("ASCII码查询".decode('gbk').encode('utf8'))
        #self.root.geometry('470x320')
        ########
        self.frm = Frame(self.root)
        #Top
        Label(self.root, text="ASCII码查询".decode('gbk').encode('utf8'), font=('Arial', 15)).pack()
        self.load_sys()
        self.frm = Frame(self.root)
        #Left
        self.frm_L = Frame(self.frm)
        self.frm_LT = Frame(self.frm_L)
        self.var_char = StringVar()
        Entry(self.frm_LT, textvariable=self.var_char, width = 5, font =('Verdana',15)).pack(side=RIGHT)
        Label(self.frm_LT, text = '字符'.decode('gbk').encode('utf8'), font =('Arial',12)).pack(side=LEFT)
        self.frm_LT.pack()

        self.var_L_char = StringVar()
        self.lb_char = Listbox(self.frm_L, selectmode=BROWSE, listvariable=self.var_L_char, font =('Verdana',12), width=10, height=13)
        self.lb_char.bind('<ButtonRelease-1>', self.get_char)
        for key in self.char_num:
            self.lb_char.insert(END, key[0])
        self.scrl_char = Scrollbar(self.frm_L)
        self.scrl_char.pack(side=RIGHT, fill=Y)
        self.lb_char.configure(yscrollcommand = self.scrl_char.set)
        self.lb_char.pack(side=LEFT, fill=BOTH)
        self.scrl_char['command'] = self.lb_char.yview

        self.frm_L.pack(side = LEFT)

        #Mid
        self.frm_M = Frame(self.frm)
        self.t_show = Text(self.frm_M, width=20, height=5, font =('Verdana',15))
        self.t_show.insert('1.0', '')
        self.t_show.pack()

        self.frm_MB = Frame(self.frm_M)
        Button(self.frm_MB, text="清除".decode('gbk').encode('utf-8'), command=self.clear, width=6, height=1, font=('Arial', 10)).pack(side=LEFT)
        Button(self.frm_MB, text="查询".decode('gbk').encode('utf-8'), command=self.search, width=6, height=1, font=('Arial', 10)).pack(side=RIGHT)
        self.frm_MB.pack(side=BOTTOM)

        self.frm_M.pack(side=LEFT)
        
        #Right
        self.frm_R = Frame(self.frm)
        self.frm_RT = Frame(self.frm_R)
        self.var_int = StringVar()
        Entry(self.frm_RT, textvariable=self.var_int, width=5, font =('Verdana',15)).pack(side=LEFT)
        Label(self.frm_RT, text='十进制'.decode('gbk').encode('utf-8'), font =('Arial',12)).pack(side=RIGHT)
        self.frm_RT.pack()
        self.var_R_int = StringVar()
        self.lb_int = Listbox(self.frm_R, selectmode=BROWSE, listvariable=self.var_R_int, font =('Verdana',12), width=10, height=13)
        self.lb_int.bind('<ButtonRelease-1>', self.get_int,)
        for key in self.num_char:
            self.lb_int.insert(END, key[0])
        self.scrl_int = Scrollbar(self.frm_R)
        self.scrl_int.pack(side=RIGHT, fill=Y)
        self.lb_int.configure(yscrollcommand = self.scrl_int.set)
        self.lb_int.pack(side=LEFT, fill=BOTH)
        self.scrl_int['command'] = self.lb_int.yview

        self.frm_R.pack(side = LEFT)

        self.frm.pack()
        ########

        
    def get_char(self, event):
        self.var_char.set('')
        self.var_int.set('')
        tmp = self.lb_char.get(self.lb_char.curselection())
        self.var_char.set(tmp)
    def get_int(self, event):
        self.var_int.set('')
        self.var_char.set('')
        tmp = self.lb_int.get(self.lb_int.curselection())
        self.var_int.set(tmp)
    def clear(self):
        self.var_char.set('')
        self.var_int.set('')
        self.t_show.delete('1.0', '10.0')
    def search(self):
        self.t_show.delete('1.0', '100.0')
        tmp_char = self.var_char.get()
        tmp_int = self.var_int.get()
        if tmp_char != '':
            if not self.char_info_hash.has_key(tmp_char):
                self.t_show.insert('1.0', "您输入的字符不在128个字符之内".decode('gbk').encode('utf8'))
            else:
                self.t_show.insert('1.0', '十六进制:'.decode('gbk').encode('utf8') + '\t' + self.char_info_hash[tmp_char][2] + '\n')
                self.t_show.insert('1.0', '十进制:'.decode('gbk').encode('utf8') +'\t' + self.char_info_hash[tmp_char][1] + '\n')
                self.t_show.insert('1.0', '八进制:'.decode('gbk').encode('utf8') + '\t' + self.char_info_hash[tmp_char][0] + '\n')
                self.t_show.insert('1.0', '字符:'.decode('gbk').encode('utf8') +'\t' + tmp_char + '\n\n')
            self.var_char.set('')
            self.var_int.set('')
        elif tmp_int !='':
            if not self.num_info_hash.has_key(tmp_int):
                self.t_show.insert('1.0', "请输入介于0~127之间的整数".decode('gbk').encode('utf8'))
            else:
                self.t_show.insert('1.0', '字符:'.decode('gbk').encode('utf8') +'\t' + self.num_info_hash[tmp_int][2] + '\n')
                self.t_show.insert('1.0', '十六进制:'.decode('gbk').encode('utf8') + '\t' + self.num_info_hash[tmp_int][1] + '\n')
                self.t_show.insert('1.0', '八进制:'.decode('gbk').encode('utf8') + '\t' + self.num_info_hash[tmp_int][0] + '\n')
                self.t_show.insert('1.0', '十进制:'.decode('gbk').encode('utf8') + '\t' + tmp_int + '\n\n')
            self.var_char.set('')
            self.var_int.set('')
        else:
            self.t_show.insert('1.0', '请选择或输入'.decode('gbk').encode('utf8'))
        
    def load_sys(self):
        f = file('asc')
        for line in f:
            chunk = line.strip().split('\t')
            self.num_char[int(chunk[1])] = chunk[3]
            self.char_num[chunk[3]] = int(chunk[1])
            self.num_info_hash[chunk[1]] = [chunk[0], chunk[2], chunk[3]]
            self.char_info_hash[chunk[3]] = [chunk[0], chunk[1], chunk[2]]

        self.num_char =sorted(self.num_char.iteritems(), key = lambda asd:asd[0])
        self.char_num =sorted(self.char_num.iteritems(), key = lambda asd:asd[1])




def main():
    d = show()
    mainloop()
if __name__== "__main__":
    main()
'''




