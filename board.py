import tkinter
import sys
from tkinter import ttk

#掲示板を作り変える関数
def createwindow():
    #会場名変更
    joumei.configure(text = "\n".join(box1.get()))
    if (box2.get() == '10') or (box2.get() == '11') or (box2.get() == '12'):
        race1.configure(text = box2.get(),font=("MSゴシック", "50", "bold"))
        race1.place(x = 75, y = 23)
    else:
        race1.configure(text = box2.get(),font=("MSゴシック", "70", "bold"))
        race1.place(x = 85, y = 8)

    #馬番変更
    first_h.configure(text = box3.get())
    second_h.configure(text = box4.get())
    third_h.configure(text = box5.get())
    fourth_h.configure(text = box6.get())
    fifth_h.configure(text = box7.get())

    #馬場状態変更
    siba2.configure(text = box12.get())
    dirt2.configure(text = box13.get())

    #確定状況変更
    if box14.get() == '確定':
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = 'red')
    elif box14.get() == '審議':
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = 'blue')
    else:
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = '#696969')
    
    #着差変更
    first_s.configure(text = box8.get())
    second_s.configure(text = box9.get())
    third_s.configure(text = box10.get())
    fourth_s.configure(text = box11.get())

    #レコード変更
    record.configure(text = box15.get())

    #タイム変更
    time_min.configure(text = box16.get())
    time_sec.configure(text = box17.get())
    time_sec10.configure(text = box18.get())

    #4ハロン変更
    fourf_sec.configure(text = box19.get())
    fourf_sec10.configure(text = box20.get())

    #3ハロン変更
    threef_sec.configure(text = box21.get())
    threef_sec10.configure(text = box22.get())

    #同着処理
    if box8.get() == '同着': #1着同着の場合
        second.configure(text = 'Ⅰ')
        same = 1
    else:
        second.configure(text = 'Ⅱ')
        same = 0

    if box9.get() == '同着': #2着同着の場合
        if same == 1:
            third.configure(text = 'Ⅰ')
        elif same == 0:
            third.configure(text = 'Ⅱ')
            same = 2
    else:
        third.configure(text = 'Ⅲ')
        same = 0

    if box10.get() == '同着': #3着同着の場合
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

    if box11.get() == '同着': #4着同着の場合
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

#ウィンドウ作成
#設定画面
root = tkinter.Tk()
root.geometry('250x550')
root.title('設定画面')
#着順掲示板
root2 = tkinter.Tk()
root2.geometry('500x850')
root2.configure(bg = 'black')
root2.title('掲示板')
canvas = tkinter.Canvas(root2, bg = 'black', height = 900, width = 500 )

#root(表示内容の設定)のウィジェット
#場名の設定
label1 = tkinter.Label(root, text = '場名')
box1 = ttk.Combobox(root,  values=['　　','東京','中山','阪神','京都','中京','小倉','新潟','福島','札幌','函館'], width = 4)

#馬番の設定
label2 = tkinter.Label(root, text = 'R')
box2 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12], width = 2)
label3 =tkinter.Label(root, text = '1')
box3 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
label4 = tkinter.Label(root, text = '2')
box4 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
label5 = tkinter.Label(root, text = '3')
box5 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
label6 = tkinter.Label(root, text = '4')
box6 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
label7 = tkinter.Label(root, text = '5')
box7 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)

#着差の設定
label8 =tkinter.Label(root, text = '1,2')
box8 = tkinter.Entry(root)
label9 =tkinter.Label(root, text = '2,3')
box9 = tkinter.Entry(root)
label10 =tkinter.Label(root, text = '3,4')
box10 = tkinter.Entry(root)
label11 =tkinter.Label(root, text = '4,5')
box11 = tkinter.Entry(root)

#馬場状態の設定
label12 = tkinter.Label(root, text = '芝')
box12 = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)
label13 = tkinter.Label(root, text = 'ダート')
box13 = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)

#確定状況の設定
label14 = tkinter.Label(root, text = '状況')
box14 = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4)

#タイム関連の設定
label15 = tkinter.Label(root, text = 'レコード')
box15 = ttk.Combobox(root, state="readonly", values=['　','ﾚｺｰﾄﾞ','ﾃｽﾄ*'], width = 4)
#入線タイム
label16 =tkinter.Label(root, text = 'time min.')
box16 = tkinter.Entry(root)
label17 =tkinter.Label(root, text = 'time sec')
box17 = tkinter.Entry(root)
label18 =tkinter.Label(root, text = 'time sec 1/10')
box18 = tkinter.Entry(root)
#4ハロン
label19 =tkinter.Label(root, text = '4F sec')
box19 = tkinter.Entry(root)
label20 =tkinter.Label(root, text = '4F sec 1/10')
box20 = tkinter.Entry(root)
#3ハロン
label21 =tkinter.Label(root, text = '3F sec')
box21 = tkinter.Entry(root)
label22 =tkinter.Label(root, text = '3F sec 1/10')
box22 = tkinter.Entry(root)

#設定内容の反映ボタン
createbutton = tkinter.Button(root, text = 'create' ,command = createwindow)

#プログラム終了用のボタン
exitbutton = tkinter.Button(root, text = 'exit' , command = sys.exit)

#root2(掲示板)のウィジェット
#場名
joumei = tkinter.Label(root2,text="\n".join('　　'), font=("MSゴシック", "33", "bold"), foreground = 'white', bg = 'black')

#レース番号
race1 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), foreground = 'yellow', bg = 'black' )
race2 = tkinter.Label(root2,text = 'R', font=("MSゴシック", "40", "bold"), foreground = 'white', bg = 'black' )

#着順
first = tkinter.Label(root2,text = 'Ⅰ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
second = tkinter.Label(root2,text = 'Ⅱ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
third = tkinter.Label(root2,text = 'Ⅲ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fourth = tkinter.Label(root2,text = 'Ⅳ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fifth = tkinter.Label(root2,text = 'Ⅴ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')

#馬番
first_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
second_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
third_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fourth_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fifth_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')

#馬場状態
siba1 = tkinter.Label(root2,text = '芝', font=("MSゴシック", "33", "bold"), width = 2,foreground = 'white' ,bg = 'black')
siba2 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
dirt1 = tkinter.Label(root2,text = 'ダート', font=("MSゴシック", "33", "bold"), foreground = 'white' ,bg = 'black')
dirt2 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')

#確定状況
now = tkinter.Label(root2,text = ' ', font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = '#696969')

#着差
first_s = tkinter.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
second_s = tkinter.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
third_s = tkinter.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
fourth_s = tkinter.Label(root2,text = ' ', font=("MSゴシック", "40", "bold"), width = 4,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
record = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 4,foreground = 'red' ,bg = '#696969')

#タイム関連
time = tkinter.Label(root2,text = 'タイム', font=("MSゴシック", "27", "bold"), foreground = 'white' ,bg = 'black')
fourf = tkinter.Label(root2,text = '４Ｆ', font=("MSゴシック", "27", "bold"),foreground = 'white' ,bg = 'black')
threef = tkinter.Label(root2,text = '３Ｆ', font=("MSゴシック", "27", "bold"), foreground = 'white' ,bg = 'black')
#入線タイム
time_min = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
time_sec = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
time_sec10 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
dot = tkinter.Label(root2,text = '.', font=("MSゴシック", "30", "bold"),width = 1, foreground = 'white' ,bg = 'black')
dot2 = tkinter.Label(root2,text = '.', font=("MSゴシック", "30", "bold"),width = 1, foreground = 'white' ,bg = 'black')
dot3 = tkinter.Label(root2,text = '.', font=("MSゴシック", "30", "bold"),width = 1, foreground = 'white' ,bg = 'black')
dot4 = tkinter.Label(root2,text = '.', font=("MSゴシック", "30", "bold"),width = 1, foreground = 'white' ,bg = 'black')
none = tkinter.Label(root2,text = '', font=("MSゴシック", "1", "bold"),width = 1, foreground = 'white' ,bg = 'black')
none2 = tkinter.Label(root2,text = '', font=("MSゴシック", "1", "bold"),width = 1, foreground = 'white' ,bg = 'black')
none3 = tkinter.Label(root2,text = '', font=("MSゴシック", "1", "bold"),width = 1, foreground = 'white' ,bg = 'black')
#4ハロン
fourf_sec = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
fourf_sec10 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')
#3ハロン
threef_sec = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969')
threef_sec10 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "45", "bold"), width = 1,foreground = 'yellow' ,bg = '#696969')

#着順の後ろに表示する円
canvas.create_oval(10,120,90,200,fill = 'blue')
canvas.create_oval(10,210,90,290,fill = 'blue')
canvas.create_oval(10,300,90,380,fill = 'blue')
canvas.create_oval(10,390,90,470,fill = 'blue')
canvas.create_oval(10,480,90,560,fill = 'blue')

#円を配置
canvas.pack()

#設定画面のウイジェットを配置
label1.grid(column = 0 ,row = 0)
box1.grid(column = 1, row = 0, )
label2.grid(column = 0 ,row = 1)
box2.grid(column = 1, row = 1)
label3.grid(column = 0 ,row = 2)
box3.grid(column = 1, row = 2,)
label4.grid(column = 0 ,row = 3)
box4.grid(column = 1, row = 3)
label5.grid(column = 0 ,row = 4)
box5.grid(column = 1, row = 4)
label6.grid(column = 0 ,row = 5)
box6.grid(column = 1, row = 5)
label7.grid(column = 0 ,row = 6)
box7.grid(column = 1, row = 6)
label8.grid(column = 0 ,row = 7)
box8.grid(column = 1, row = 7)
label9.grid(column = 0 ,row = 8)
box9.grid(column = 1, row = 8)
label10.grid(column = 0 ,row = 9)
box10.grid(column = 1, row = 9)
label11.grid(column = 0 ,row = 10)
box11.grid(column = 1, row = 10)
label12.grid(column = 0 ,row = 11)
box12.grid(column = 1, row = 11)
label13.grid(column = 0 ,row = 12)
box13.grid(column = 1, row = 12)
label14.grid(column = 0 ,row = 13)
box14.grid(column = 1, row = 13)
label15.grid(column = 0 ,row = 14)
box15.grid(column = 1, row = 14)
label16.grid(column = 0 ,row = 15)
box16.grid(column = 1, row = 15)
label17.grid(column = 0 ,row = 16)
box17.grid(column = 1, row = 16)
label18.grid(column = 0 ,row = 17)
box18.grid(column = 1, row = 17)
label19.grid(column = 0 ,row = 18)
box19.grid(column = 1, row = 18)
label20.grid(column = 0 ,row = 19)
box20.grid(column = 1, row = 19)
label21.grid(column = 0 ,row = 20)
box21.grid(column = 1, row = 20)
label22.grid(column = 0 ,row = 21)
box22.grid(column = 1, row = 21)
createbutton.grid(column = 0, row = 22)
exitbutton.grid(column = 1, row = 22)

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
dot2.place(x = 425, y = 623, height = 100)
time_sec10.place(x = 452, y = 630,height = 55)
none.place(x = 490, y = 623, height = 100)
fourf_sec.place(x = 350, y = 700, height = 55)
dot3.place(x = 425, y = 693, height = 100)
fourf_sec10.place(x = 452, y = 700, height = 55)
none2.place(x = 490, y = 693, height = 100)
threef_sec.place(x = 350, y = 770, height = 55)
dot4.place(x = 425, y = 773, height = 75)
threef_sec10.place(x = 452, y = 770, height = 55)
none3.place(x = 490, y = 763, height = 80)

#実行
root.mainloop()
root2.mainloop()