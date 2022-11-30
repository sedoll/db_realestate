from tkinter import *
import tkinter as tk
import tkinter.ttk
import os
from collections import Counter

window = Tk()

window.title("Naver Store management program")

#################################################

notebook=tkinter.ttk.Notebook(window, width=800, height=500)
notebook.pack()

tab1=tkinter.Frame(window)
notebook.add(tab1, text=" Trading ")
tab2=tkinter.Frame(window)
notebook.add(tab2, text="Gomming")
tab3=tkinter.Frame(window)
notebook.add(tab3, text="    ???    ")

def closing(event):
    window.destroy()
    os.system('C:\\gom\\python gom_gui.py')
    
lb_hi = Label(tab2, text="Reboot", bg='gray19', fg='gray60',width=10, height=3)
lb_hi.bind('<Button-1>',closing)
lb_hi.place(x=10,y=10)

entry = tk.Entry(tab2,fg="gray19", bg="snow", width=20)
blog='blog.naver.com/xenostep'
entry.insert(0,blog)
entry.place(x=10,y=80)

entry1 = tk.Entry(tab2,fg="gray19", bg="snow", width=20)
entry1.insert(0, entry.get().split("/")[1])
entry1.place(x=10,y=100)



def cus():
    cus_list = []
    with open('C:\\gom\\gom.txt') as cus:
        for line in cus:
            cus_list.append(line)

    cus_list = cus_list[2:]

    for i in range(len(cus_list)):
        cus_all.insert(INSERT, cus_list[i])
    cus_all1.insert(INSERT, '\n'+Counter(cus_list).most_common(1)[0][0])

def clear():
    cus_all.delete(0.0,10.0)
    cus_all1.delete(0.0,3.0)

cus_all = tk.Text(tab2, width=20, height=10)
cus_all.place(x=200, y=100)
cus_all1 = tk.Text(tab2, width=20, height=3)
cus_all1.place(x=400, y=100)

load_bt = tk.Button(tab2, text='Load', bg='gray19', fg='snow', width=10, command=cus)
load_bt.place(x=300, y=400)
clear_bt = tk.Button(tab2, text='Clear', bg='royalblue', fg='snow', width=7, command=clear)
clear_bt.place(x=385, y=400)
save_bt = tk.Button(tab2, text='Save', bg='gray19', fg='snow', width=10)
save_bt.place(x=450, y=400)
lb_hi = Label(tab2, text="->",fg='gray19')
lb_hi.place(x=360,y=110)

def new_win(event):
    nw=Tk()
    nw.title("Select video")

    def closer(event):
        nw.destroy()
    nw.bind("<Escape>", closer)

    nw.geometry('300x300+300+100')
    nw.mainloop()

window.geometry('800x500+300+100')
window.mainloop()