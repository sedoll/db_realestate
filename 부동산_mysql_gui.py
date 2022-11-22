# GUI를 활용한 부동산 가격 조회

import pymysql
from tkinter import *
import tkinter.ttk as ttk

values = ['', '두정동', '백석동', '성거읍', '구성동', '다가동', '목천읍', '전체']

d = {'': [''],
    '성거읍': ['문덕리', '신월리'],
    '목천읍': ['삼성리', '서리'],}

def changeDong():
    container1.readonly_combobox2["values"] = d[container1.readonly_combobox1.get()]

def selectData():
    data1, data2, data3, data4 = [], [], [], []
    sql = ''
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='real_estate', charset='utf8')
    cur = conn.cursor()
    
    sql = f"SELECT 시군구, 번지, 본번, 부번 FROM city"
    cur.execute(sql)
    
    while True:
        row = cur.fetchone()
        if row == None:
            break
        data1.append(row[0]); data2.append(row[1]); data3.append(row[2]); data4.append(row[3])
        
    listData1.delete(0, listData1.size()-1); listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1); listData4.delete(0, listData4.size()-1)
    
    for i1, i2, i3, i4 in zip(data1, data2, data3, data4):
        listData1.insert(END, i1); listData2.insert(END, i2)
        listData3.insert(END, i3); listData4.insert(END, i4)
        
    conn.close()

class Cont1:
    def __init__(self, frame):
        global select
        self.inframe = Frame(frame)
        self.inframe.pack(fill=X, anchor=N)
        # 읽기만 되는 combobox
        self.label1 = Label(self.inframe, width=5, text='읍면동')
        self.label1.pack(side=LEFT)
        self.readonly_combobox1 = ttk.Combobox(self.inframe, width=5, values=values, state='readonly')
        self.readonly_combobox1.current(0) # 0번째 인덱스값 선택
        self.readonly_combobox1.pack(side=LEFT)
        self.btnGu = Button(self.inframe, text='선택', command=changeDong)
        self.btnGu.pack(side=LEFT, padx=5, pady=10)

        self.label2 = Label(self.inframe, width=5, text='리')
        self.label2.pack(side=LEFT)
        self.readonly_combobox2 = ttk.Combobox(self.inframe, width=5, values=d[self.readonly_combobox1.get()], state='readonly')
        self.readonly_combobox2.current(0) # 0번째 인덱스값 선택
        self.readonly_combobox2.pack(side=LEFT)

        self.label4 = Label(self.inframe, width=5, text='번지')
        self.label4.pack(side=LEFT)
        self.edt4 = Entry(self.inframe, width=10)
        self.edt4.pack(side=LEFT, padx=10, pady=10)
        
        self.label5 = Label(self.inframe, width=5, text='본번')
        self.label5.pack(side=LEFT)
        self.edt5 = Entry(self.inframe, width=10)
        self.edt5.pack(side=LEFT, padx=10, pady=10)
        
        self.label6 = Label(self.inframe, width=5, text='부번')
        self.label6.pack(side=LEFT)
        self.edt6 = Entry(self.inframe, width=10)
        self.edt6.pack(side=LEFT, padx=10, pady=10)

root = Tk()
root.geometry('1000x500')
root.title('천안시 부동산 거래가 확인 프로그램')
root.resizable(False, False)

edtFrame = Frame(root)
edtFrame.pack()
labelFrame = Frame(root)
labelFrame.pack(side = TOP, fill=BOTH)
listFrame = Frame(root)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

container1 = Cont1(edtFrame)


label1 = Label(labelFrame, text='아파트이름')
label1.pack(side=LEFT, fill=BOTH, expand=1)
label2 = Label(labelFrame, text='가격')
label2.pack(side=LEFT, fill=BOTH, expand=1)
label3 = Label(labelFrame, text='건축연도')
label3.pack(side=LEFT, fill=BOTH, expand=1)
label4 = Label(labelFrame, text='근처역')
label4.pack(side=LEFT, fill=BOTH, expand=1)

listData1 = Listbox(listFrame, bg='#AAAAAA')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg='#AAAAAA')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg='#AAAAAA')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg='#AAAAAA')
listData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()