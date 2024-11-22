import tkinter as tk
from tkinter import ttk
import sys

#掲示板を作り変える関数
def createwindow():
    #会場名変更
    joumei.configure(text = "\n".join(box[0].get()))
    if (len(box[1].get()) == 2):
        race1.configure(text = box[1].get(),font=("MSゴシック", "50", "bold"))
        race1.place(x = 75, y = 23)
    else:
        race1.configure(text = box[1].get(),font=("MSゴシック", "70", "bold"))
        race1.place(x = 85, y = 8)

    #馬番変更
    first_h.configure(text = box[2].get())
    second_h.configure(text = box[3].get())
    third_h.configure(text = box[4].get())
    fourth_h.configure(text = box[5].get())
    fifth_h.configure(text = box[6].get())
    
    #着差変更
    first_s.configure(text = box[7].get())
    second_s.configure(text = box[8].get())
    third_s.configure(text = box[9].get())
    fourth_s.configure(text = box[10].get())

    #同着処理
    if box[7].get() == '同着': #1着同着の場合
        second.configure(text = 'Ⅰ')
        same = 1
    else:
        second.configure(text = 'Ⅱ')
        same = 0

    if box[8].get() == '同着': #2着同着の場合
        if same == 1:
            third.configure(text = 'Ⅰ')
        elif same == 0:
            third.configure(text = 'Ⅱ')
            same = 2
    else:
        third.configure(text = 'Ⅲ')
        same = 0

    if box[9].get() == '同着': #3着同着の場合
        if same == 1:
            fourth.configure(text = 'Ⅰ')
        elif same == 2:
            fourth.configure(text = 'Ⅱ')
        elif same == 0:
            fourth.configure(text = 'Ⅲ')
            same = 3
    else:
        fourth.configure(text = 'Ⅳ')
        same = 4

    if box[10].get() == '同着': #4着同着の場合
        if same == 1:
            fifth.configure(text = 'Ⅰ')
        elif same == 2:
            fifth.configure(text = 'Ⅱ')
        elif same == 3:
            fifth.configure(text = 'Ⅲ')
        elif same == 4:
            fifth.configure(text = 'Ⅳ')
    else:
        fifth.configure(text = 'Ⅴ')

    #馬場状態変更
    siba2.configure(text = box[11].get())
    dirt2.configure(text = box[12].get())

    #確定状況変更
    if ((text := box[13].get()) == '確定'):
        now.configure(text = text, font=("MSゴシック", "90", "bold"), width = 3, foreground = 'white', bg = 'red')
    elif (text == '審議'):
        now.configure(text = text, font=("MSゴシック", "90", "bold"), width = 3, foreground = 'white', bg = 'blue')
    else:
        now.configure(text = "", font=("MSゴシック", "90", "bold"), width = 3, foreground = 'white', bg = '#696969')

    #レコード変更
    record.configure(text = box[14].get())

    #タイム変更
    time_min.configure(text = box[15].get())
    time_sec.configure(text = box[16].get())
    time_sec10.configure(text = box[17].get())

    #4ハロン変更
    fourf_sec.configure(text = box[18].get())
    fourf_sec10.configure(text = box[19].get())

    #3ハロン変更
    threef_sec.configure(text = box[20].get())
    threef_sec10.configure(text = box[21].get())

#ウィジェットの複製関数
def clone(widget):
    parent = widget.nametowidget(widget.winfo_parent())
    cls = widget.__class__

    clone = cls(parent)
    for key in widget.configure():
        clone.configure({key: widget.cget(key)})
    return clone

#入力できる数字の制限
def validate_input(n, limit):
    if (n.isdigit()):
        return int(n) <= int(limit)
    else:
        return n == ""

#ウィンドウ作成
#設定画面
root = tk.Tk()
root.geometry('250x500')
root.resizable(False, False)
root.title('設定画面')

#着順掲示板
root2 = tk.Tk()
root2.geometry('510x850')
root2.resizable(False, False)
root2.configure(bg = 'black')
root2.title('掲示板')
canvas = tk.Canvas(root2, bg = 'black', height = 900, width = 500 )

#root(表示内容の設定)のウィジェット
labels = []
box = []
vc = root.register(validate_input)
#場名の設定
labels.append(tk.Label(root, text = '場名'))
box.append(ttk.Combobox(root,  values=['　　','東京','中山','阪神','京都','中京','小倉','新潟','福島','札幌','函館'], width = 4))

#レース番号の設定
labels.append(tk.Label(root, text = 'レース数'))
box.append(tk.Entry(root, validate="key", validatecommand=(vc, "%P", 12), width = 3))

#馬番の設定
[labels.append(tk.Label(root, text = str(i) + "着馬")) for i in range(1,6)]
[box.append(tk.Entry(root, validate="key", validatecommand=(vc, "%P", 18), width = 3)) for i in range(5)]

#着差の設定
[labels.append(tk.Label(root, text = '着差' + str(i) + "," + str(i+1))) for i in range(1,5)]
[box.append(tk.Entry(root)) for i in range(4)]

#馬場状態の設定
labels.append(tk.Label(root, text = '芝'))
labels.append(tk.Label(root, text = 'ダート'))
[box.append(ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)) for i in range(2)]

#確定状況の設定
labels.append(tk.Label(root, text = '状況'))
box.append(ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4))

#タイム関連の設定
labels.append(tk.Label(root, text = 'レコード'))
box.append(ttk.Combobox(root, state="readonly", values=['　','ﾚｺｰﾄﾞ','ﾃｽﾄ*'], width = 4))
#入線タイム
labels.append(tk.Label(root, text = 'time min.'))
box.append(tk.Entry(root, validate="key", validatecommand=(vc, "%P", 9), width = 2))
labels.append(tk.Label(root, text = 'time sec'))
labels.append(tk.Label(root, text = 'time sec 1/10'))
#4ハロン
labels.append(tk.Label(root, text = '4F sec'))
labels.append(tk.Label(root, text = '4F sec 1/10'))
#3ハロン
labels.append(tk.Label(root, text = '3F sec'))
labels.append(tk.Label(root, text = '3F sec 1/10'))

for i in range(3):
    box.append(tk.Entry(root, validate="key", validatecommand=(vc, "%P", 59), width = 3))
    box.append(tk.Entry(root, validate="key", validatecommand=(vc, "%P", 9), width = 3))

#設定内容の反映ボタン
createbutton = tk.Button(root, text = 'create' ,command = createwindow)

#プログラム終了用のボタン
exitbutton = tk.Button(root, text = 'exit' , command = sys.exit)

#root2(掲示板)のウィジェット
#場名
joumei = tk.Label(root2,text="\n".join('　　'), font=("MSゴシック", "33", "bold"), foreground = 'white', bg = 'black')

#レース番号
race1 = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), foreground = 'yellow', bg = 'black' )
race2 = tk.Label(root2,text = 'R', font=("MSゴシック", "40", "bold"), foreground = 'white', bg = 'black' )

#着順
first = tk.Label(root2,text = 'Ⅰ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
second = tk.Label(root2,text = 'Ⅱ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
third = tk.Label(root2,text = 'Ⅲ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fourth = tk.Label(root2,text = 'Ⅳ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fifth = tk.Label(root2,text = 'Ⅴ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')

#馬番
first_h = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
second_h = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
third_h = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fourth_h = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fifth_h = tk.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')

#馬場状態
siba1 = tk.Label(root2,text = '芝', font=("MSゴシック", "33", "bold"), width = 2,foreground = 'white' ,bg = 'black')
siba2 = tk.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
dirt1 = tk.Label(root2,text = 'ダート', font=("MSゴシック", "33", "bold"), foreground = 'white' ,bg = 'black')
dirt2 = tk.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')

#確定状況
now = tk.Label(root2,text = ' ', font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = '#696969')

#着差
first_s = tk.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
second_s = tk.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
third_s = tk.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
fourth_s = tk.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
record = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 4,foreground = 'red' ,bg = '#696969')

#タイム関連
time = tk.Label(root2,text = 'タイム', font=("MSゴシック", "27", "bold"), foreground = 'white' ,bg = 'black')
fourf = tk.Label(root2,text = '４Ｆ', font=("MSゴシック", "27", "bold"),foreground = 'white' ,bg = 'black')
threef = tk.Label(root2,text = '３Ｆ', font=("MSゴシック", "27", "bold"), foreground = 'white' ,bg = 'black')
#入線タイム
time_min = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
time_sec = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
time_sec10 = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
dot = tk.Label(root2,text = '.', font=("MSゴシック", "30", "bold"),width = 1, foreground = 'white' ,bg = 'black')
#4ハロン
fourf_sec = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
fourf_sec10 = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
#3ハロン
threef_sec = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
threef_sec10 = tk.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')

#着順の後ろに表示する円
canvas.create_oval(10,120,90,200,fill = 'blue')
canvas.create_oval(10,210,90,290,fill = 'blue')
canvas.create_oval(10,300,90,380,fill = 'blue')
canvas.create_oval(10,390,90,470,fill = 'blue')
canvas.create_oval(10,480,90,560,fill = 'blue')

#円を配置
canvas.pack()

#設定画面のウイジェットを配置
[labels[i].grid(column = 0, row = i) for i in range(len(labels))]
[box[i].grid(column = 1, row = i) for i in range(len(box))]
createbutton.grid(column = 0, row = len(labels))
exitbutton.grid(column = 1, row = len(labels))

#掲示板のウィジェットを配置
joumei.place(x = 20, y = 10)
race1.place(x = 80, y = 11)
race2.place(x = 150, y = 35)
first.place(x = 24, y = 132)
second.place(x = 24, y = 222)
third.place(x = 24, y = 312)
fourth.place(x = 24, y = 402)
fifth.place(x = 24, y = 492)
first_h.place(x = 100, y = 125, height = 72)
second_h.place(x = 100, y = 215, height = 72)
third_h.place(x = 100, y = 305, height = 72)
fourth_h.place(x = 100, y = 395, height = 72)
fifth_h.place(x = 100, y = 485, height = 72)
siba1.place(x = 60, y = 560)
siba2.place(x = 15, y = 610, height = 75)
dirt1.place(x = 22, y = 700)
dirt2.place(x = 15, y = 750, height = 75)
now.place(x = 250 , y = 10, height = 120)
first_s.place(x = 290, y = 165, height = 60)
second_s.place(x = 290, y = 260, height = 60)
third_s.place(x = 290, y = 355, height = 60)
fourth_s.place(x = 290, y = 450, height = 60)
record.place(x = 290, y = 550, height = 55)
time.place(x = 170, y = 645)
fourf.place(x = 205, y = 715)
threef.place(x = 205, y = 780)
time_min.place(x = 283, y = 630, height = 55)
dot.place(x = 323, y = 623, height = 100)
time_sec.place(x = 350, y = 630, height = 55)
clone(dot).place(x = 425, y = 623, height = 100)
time_sec10.place(x = 452, y = 630,height = 55)
fourf_sec.place(x = 350, y = 700, height = 55)
clone(dot).place(x = 425, y = 693, height = 100)
fourf_sec10.place(x = 452, y = 700, height = 55)
threef_sec.place(x = 350, y = 770, height = 55)
clone(dot).place(x = 425, y = 773, height = 75)
threef_sec10.place(x = 452, y = 770, height = 55)

#実行
root.mainloop()
root2.mainloop()