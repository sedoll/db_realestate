# GUI를 활용한 부동산 가격 조회
from math import *
from tkinter import *
import tkinter.ttk as ttk
import pymysql

values = ['두정동', '백석동', '불당동', '성거읍', '성성동', '성정동', '성환읍', '신당동', '쌍용동', '와촌동', '입장면', '직산읍', '차암동', '전체']
space = 30
sql = 'SELECT name, dong, address, deal, acount, area FROM trade_view WHERE dong = %s LIMIT 20'
dong = ''

def changeDong():
    dong = str(container1.readonly_combobox1.get())
    print(dong)

# 비 역세권 고가순
def desc():
    global sql
    sql = "SELECT dong, name, address, deal, acount, area FROM trade_view WHERE dong LIKE %s AND station_area = '' ORDER BY acount DESC LIMIT 100"

# 비 역세권 저가순
def asc():
    global sql
    sql = "SELECT dong, name, address, deal, acount, area FROM trade_view WHERE dong LIKE %s AND station_area = '' ORDER BY acount LIMIT 100"

# 역세권 고가 순
def station_desc():
    global sql
    sql = "SELECT dong, name, address, deal, acount, area, station_area FROM trade_view WHERE dong LIKE %s AND station_area != '' ORDER BY acount DESC  LIMIT 100"

# 역세권 저가 순
def station_asc():
    global sql
    sql = "SELECT dong, name, address, deal, acount, area, station_area FROM trade_view WHERE dong LIKE %s AND station_area != '' ORDER BY acount LIMIT 100"

def selectData():
    print(chkt.get())
    global treelist
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='0000', db='estate', charset='utf8')
    cur = conn.cursor()
    
    search = container1.readonly_combobox1.get()
    if search != '전체':
        cur.execute(sql, (search + '%'))
    else:
        cur.execute("SELECT dong, name, address, deal, acount, area FROM trade_view ORDER BY acount DESC LIMIT 20")
    
    # sql 데이터 추출
    row = cur.fetchall()
    
    # treeview 데이터 초기화
    treeview.delete(*treeview.get_children())
    
    # 튜플 형태의 데이터를 리스트로 만들어 면적을 평으로 바꿈
    treelist = [list(row[x]) for x in range(len(row))]
    for i in range(len(treelist)):
        treelist[i][5] = int(round(treelist[i][5]) / 3.3)
        
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i])
    conn.close()

class Cont1:
    def __init__(self, frame):
        global select
        self.inframe = Frame(frame)
        self.inframe.pack(fill=X, anchor=N)
        
        # 읽기만 되는 combobox (쓰기 안됨)
        self.label1 = Label(self.inframe, width=5, text='읍면동')
        self.label1.pack(side=LEFT)
        self.readonly_combobox1 = ttk.Combobox(self.inframe, width=5, values=values, state='readonly')
        self.readonly_combobox1.current(0) # 0번째 인덱스값 선택
        self.readonly_combobox1.pack(side=LEFT)
        self.btnGu = Button(self.inframe, text='선택', command=changeDong)
        self.btnGu.pack(side=LEFT, padx=5, pady=10)
        
        self.label2 = Label(self.inframe, width=5, text='금액')
        self.label2.pack(side=LEFT)
        self.acount1 = Entry(self.inframe, width=10)
        self.acount1.insert(0, 0)
        self.acount1.pack(side=LEFT)
        self.label2 = Label(self.inframe, width=5, text='~')
        self.label2.pack(side=LEFT)
        self.acount2 = Entry(self.inframe, width=10)
        self.acount2.insert(0, 30000)
        self.acount2.pack(side=LEFT)
        self.btnGu1 = Button(self.inframe, text='선택', command=changeDong)
        self.btnGu1.pack(side=LEFT, padx=5, pady=10)
        
        self.label3 = Label(self.inframe, width=5, text='면적')
        self.label3.pack(side=LEFT)
        self.area1 = Entry(self.inframe, width=10)
        self.area1.insert(0, 0)
        self.area1.pack(side=LEFT)
        self.label4 = Label(self.inframe, width=5, text='~')
        self.label4.pack(side=LEFT)
        self.area2 = Entry(self.inframe, width=10)
        self.area2.insert(0, 100)
        self.area2.pack(side=LEFT)
        self.btnGu2 = Button(self.inframe, text='선택', command=changeDong)
        self.btnGu2.pack(side=LEFT, padx=5, pady=10)
        
        self.label5 = Label(self.inframe, width=5, text='층')
        self.label5.pack(side=LEFT)
        self.floor1 = Entry(self.inframe, width=10)
        self.floor1.insert(0, 0)
        self.floor1.pack(side=LEFT)
        self.label6 = Label(self.inframe, width=5, text='~')
        self.label6.pack(side=LEFT)
        self.floor2 = Entry(self.inframe, width=10)
        self.floor2.insert(0, 50)
        self.floor2.pack(side=LEFT)
        self.btnGu3 = Button(self.inframe, text='선택', command=changeDong)
        self.btnGu3.pack(side=LEFT, padx=5, pady=10)


class Cont2:
    def __init__(self, frame):
        global select, chkr, chkc, chkt, chksf, chkst
        self.inframe = Frame(frame)
        self.inframe.pack(fill=X, anchor=N)
        
        self.chkbox1 = Checkbutton(self.inframe, text='매매', variable=chkt)
        self.chkbox1.select()
        self.chkbox1.pack(side=LEFT, padx=5, pady=10)
        
        self.chkbox2 = Checkbutton(self.inframe, text='전세', variable=chkc)
        self.chkbox2.pack(side=LEFT, padx=5, pady=10)
        
        self.chkbox3 = Checkbutton(self.inframe, text='월세', variable=chkr)
        self.chkbox3.pack(side=LEFT, padx=5, pady=10)
        
        self.chkbox4 = Checkbutton(self.inframe, text='역세권', variable=chkst)
        self.chkbox4.select()
        self.chkbox4.pack(side=LEFT, padx=5, pady=10)
        
        self.chkbox5 = Checkbutton(self.inframe, text='비역세권', variable=chksf)
        self.chkbox5.pack(side=LEFT, padx=5, pady=10)
        
        self.btn1 = Button(self.inframe, text='저가순 조회', command=selectData)
        self.btn1.pack(side=LEFT, padx=5, pady=10)
        
        self.btn2 = Button(self.inframe, text='고가순 조회', command=selectData)
        self.btn2.pack(side=LEFT, padx=5, pady=10)
        
        # self.btn = Button(self.inframe, text='조회', command=selectData)
        # self.btn.pack(side=LEFT, padx=5, pady=10)

def tv():
    treeview.column("#0", width=100, anchor="center")
    treeview.heading("#0", text="번호")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="읍면동")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="주소", anchor="center")
    
    treeview.column("#3", width=200, anchor="center")
    treeview.heading("three", text="단지명", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("four", text="매매전세월세", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("five", text="가격", anchor="center")

    treeview.column("#6", width=100, anchor="center")
    treeview.heading("six", text="평 수", anchor="center")
    
    treeview.column("#7", width=100, anchor="center")
    treeview.heading("seven", text="역", anchor="center")

root = Tk()
root.geometry('1000x500')
root.title('천안시 서북구 부동산 거래가 확인 프로그램')
root.resizable(False, False)

# 체크박스 값 저장 변수
chkt, chkc, chkr, chkst, chksf = IntVar(), IntVar(), IntVar(), IntVar(), IntVar()

edtFrame = Frame(root)
edtFrame.pack()

# 위젯 틀
container1 = Cont1(edtFrame)
container2 = Cont2(edtFrame)

# 데이터 출력 틀
treeview = ttk.Treeview(root, columns=["one", "two","three", "four", "five", "six", "seven"], displaycolumns=["one","two","three", "four", "five", "six", "seven"])
treeview.pack(side = BOTTOM, fill=BOTH, expand=1)
tv()

root.mainloop()