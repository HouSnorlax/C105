import tkinter as tk
from tkinter import ttk
import sys

#ラベルのフォントのテンプレート
def font(size):
    return ("MSゴシック", str(size), "bold")

#掲示板を作り変える関数
def createwindow():
    global board
    if (board == None or not board.winfo_exists()):
        board = tk.Toplevel()
        board.geometry('500x850')
        board.resizable(False, False)
        board.title('掲示板')
        board.configure(bg = 'black')
    
    #ラベルの宣言
    #場名
    course_b = tk.Label(board, text = "\n".join(course.get()), font = font(33), foreground = 'white', bg = 'black')
    
    #レース番号
    if (len(number := race_no.get()) == 2):
        race_no_b = tk.Label(board, text = number, font = font(50), width = 2, foreground = 'yellow', bg = 'black' )
        race_no_b.place(x = 65, y = 23)
    else:
        race_no_b = tk.Label(board, text = number, font = font(70), width = 2, foreground = 'yellow', bg = 'black' )
        race_no_b.place(x = 65, y = 8)
    race_b = tk.Label(board, text = 'R', font = font(40), foreground = 'white', bg = 'black' )

    #着順
    first_b = tk.Label(board, text = 'Ⅰ', font = font(34), foreground = 'white', bg = 'blue')
    second_b = tk.Label(board, text = 'Ⅱ', font = font(34), foreground = 'white', bg = 'blue')
    third_b = tk.Label(board, text = 'Ⅲ', font = font(34), foreground = 'white', bg = 'blue')
    fourth_b = tk.Label(board, text = 'Ⅳ', font = font(34), foreground = 'white', bg = 'blue')
    fifth_b = tk.Label(board, text = 'Ⅴ', font = font(34), foreground = 'white', bg = 'blue')

    #馬番
    first_h_b = tk.Label(board, text = first_h.get(), font = font(70), width = 2, foreground = 'yellow', bg = '#707070', anchor = 'e')
    second_h_b = tk.Label(board, text = second_h.get(), font = font(70), width = 2, foreground = 'yellow', bg = '#707070', anchor = 'e')
    third_h_b = tk.Label(board, text = third_h.get(), font = font(70), width = 2, foreground = 'yellow', bg = '#707070', anchor = 'e')
    fourth_h_b = tk.Label(board, text = fourth_h.get(), font = font(70), width = 2, foreground = 'yellow', bg = '#707070', anchor = 'e')
    fifth_h_b = tk.Label(board, text = fifth_h.get(), font = font(70), width = 2, foreground = 'yellow', bg = '#707070', anchor = 'e')
    
    #着差
    margin_12_b = tk.Label(board, text = margin_12.get(), font = font(40), width = 4, foreground = 'yellow', bg = '#707070')
    margin_23_b = tk.Label(board, text = margin_23.get(), font = font(40), width = 4, foreground = 'yellow', bg = '#707070')
    margin_34_b = tk.Label(board, text = margin_34.get(), font = font(40), width = 4, foreground = 'yellow', bg = '#707070')
    margin_45_b = tk.Label(board, text = margin_45.get(), font = font(40), width = 4, foreground = 'yellow', bg = '#707070')
    
    #馬場状態
    shiba_b = tk.Label(board, text = '芝', font = font(33), width = 2, foreground = 'white', bg = 'black')
    shiba_c_b = tk.Label(board, text = shiba_c.get(), font = font(60), width = 3, foreground = 'yellow', bg = '#707070')
    dirt_b = tk.Label(board, text = 'ダート', font = font(33), foreground = 'white', bg = 'black')
    dirt_c_b = tk.Label(board, text = dirt_c.get(), font = font(60), width = 3, foreground = 'yellow', bg = '#707070')

    #確定状況
    if ((text := kakutei.get()) == '確定'):
        kakutei_b = tk.Label(board, text = text, font = font(90), width = 3, foreground = 'white', bg = 'red')
    elif (text == '審議'):
        kakutei_b = tk.Label(board, text = text, font = font(90), width = 3, foreground = 'white', bg = 'blue')
    else:
        kakutei_b = tk.Label(board, text = ' ', font = font(90), width = 3, foreground = 'white', bg = '#707070')

    #レコード
    if var_record.get():
        record_b = tk.Label(board, text = 'ﾚｺｰﾄﾞ', font = font(45), width = 4, foreground = 'red', bg = '#707070')
    else:
        record_b = tk.Label(board, text = '', font = font(45), width = 4, foreground = 'red', bg = '#707070')
    
    #入線タイム
    time_b = tk.Label(board, text = 'タイム', font = font(27), foreground = 'white', bg = 'black')
    time_min_b = tk.Label(board, text = time_min.get(), font = font(45), width = 1, foreground = 'yellow', bg = '#707070')
    dot = tk.Label(board, text = '.', font = font(30), width = 1, foreground = 'white', bg = 'black')
    time_sec_b = tk.Label(board, text = time_sec.get(), font = font(45), width = 2, foreground = 'yellow', bg = '#707070')
    dot2 = tk.Label(board, text = '.', font = font(30), width = 1, foreground = 'white', bg = 'black')
    time_sec10_b = tk.Label(board, text = time_sec10.get(), font = font(45), width = 1, foreground = 'yellow', bg = '#707070')
    
    #4ハロン
    ff_b = tk.Label(board, text = '４Ｆ', font = font(27), foreground = 'white', bg = 'black')
    ff_sec_b = tk.Label(board, text = ff_sec.get(), font = font(45), width = 2, foreground = 'yellow', bg = '#707070')
    dot3 = tk.Label(board, text = '.', font = font(30),width = 1, foreground = 'white', bg = 'black')
    ff_sec10_b = tk.Label(board, text = ff_sec10.get(), font = font(45), width = 1, foreground = 'yellow', bg = '#707070')
    
    #3ハロン
    tf_b = tk.Label(board, text = '３Ｆ', font = font(27), foreground = 'white', bg = 'black')
    tf_sec_b = tk.Label(board, text = tf_sec.get(), font = font(45), width = 2, foreground = 'yellow', bg = '#707070')
    dot4 = tk.Label(board,text = '.', font = font(30), width = 1, foreground = 'white', bg = 'black')
    tf_sec10_b = tk.Label(board, text = tf_sec10.get(), font = font(45), width = 1, foreground = 'yellow', bg = '#707070')

    #ラベルの配置
    course_b.place(x = 20, y = 10) #場名
    
    race_b.place(x = 150, y = 35) #R
    
    first_b.place(x = 24, y = 132) #着順
    second_b.place(x = 24, y = 222)
    third_b.place(x = 24, y = 312)
    fourth_b.place(x = 24, y = 402)
    fifth_b.place(x = 24, y = 492)
    
    first_h_b.place(x = 100, y = 125, height = 72) #馬番
    second_h_b.place(x = 100, y = 215, height = 72)
    third_h_b.place(x = 100, y = 305, height = 72)
    fourth_h_b.place(x = 100, y = 395, height = 72)
    fifth_h_b.place(x = 100, y = 485, height = 72)
    
    margin_12_b.place(x = 290, y = 165, height = 60) #着差
    margin_23_b.place(x = 290, y = 260, height = 60)
    margin_34_b.place(x = 290, y = 355, height = 60)
    margin_45_b.place(x = 290, y = 450, height = 60)
    
    shiba_b.place(x = 60, y = 560) #馬場状態
    shiba_c_b.place(x = 15, y = 610, height = 75)
    dirt_b.place(x = 22, y = 700)
    dirt_c_b.place(x = 15, y = 750, height = 75)
    
    kakutei_b.place(x = 250 , y = 10, height = 120) #確定状況

    record_b.place(x = 290, y = 550, height = 55) #レコード
    
    time_b.place(x = 170, y = 645) #入線タイム
    time_min_b.place(x = 283, y = 630, height = 55)
    dot.place(x = 323, y = 623, height = 100)
    time_sec_b.place(x = 350, y = 630, height = 55)
    dot2.place(x = 425, y = 623, height = 100)
    time_sec10_b.place(x = 452, y = 630,height = 55)

    ff_b.place(x = 205, y = 715) #4ハロン
    ff_sec_b.place(x = 350, y = 700, height = 55)
    dot3.place(x = 425, y = 693, height = 100)
    ff_sec10_b.place(x = 452, y = 700, height = 55)
    
    tf_b.place(x = 205, y = 780) #3ハロン
    tf_sec_b.place(x = 350, y = 770, height = 55)
    dot4.place(x = 425, y = 770, height = 78)
    tf_sec10_b.place(x = 452, y = 770, height = 55)



#サブウィンドウを先に定義する
board = None

#ウィンドウを作成
root = tk.Tk()
root.geometry('225x500')
root.resizable(False, False)
root.title('設定画面')

labels = [] #設定画面のテキスト用配列

#テキストの作成
labels.append(tk.Label(root, text = '場名')) #レース場名
labels.append(tk.Label(root, text = 'R'))  #レース番号

for i in range(1,6):
    labels.append(tk.Label(root, text = str(i) + "着馬")) #n着馬

for i in range(1,5):
    labels.append(tk.Label(root, text = '着差' + str(i) + "," + str(i+1))) #着差

labels.append(tk.Label(root, text = '芝')) #馬場状態
labels.append(tk.Label(root, text = 'ダート'))

labels.append(tk.Label(root, text = '状況')) #確定状況
labels.append(tk.Label(root, text = 'レコード')) 

labels.append(tk.Label(root, text = 'time min')) #入線タイム
labels.append(tk.Label(root, text = 'time sec'))
labels.append(tk.Label(root, text = 'time 1/10'))

labels.append(tk.Label(root, text = '4F sec')) #4ハロン
labels.append(tk.Label(root, text = '4F 1/10 sec'))

labels.append(tk.Label(root, text = '3F sec')) #3ハロン
labels.append(tk.Label(root, text = '3F 1/10 sec'))

#メニュー・ボックス・ボタンの作成
course = ttk.Combobox(root,  values=['　　','札幌','函館','福島','新潟','中山','東京','中京','京都','阪神','小倉'], width = 4) #レース場名

race_no = tk.Spinbox(root, from_ = 1, to = 12, width = 3) #レース番号

first_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) #馬番の入力
second_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) 
third_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) 
fourth_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) 
fifth_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3)

margin_12 = tk.Entry(root) #着差の入力
margin_23 = tk.Entry(root)
margin_34 = tk.Entry(root)
margin_45 = tk.Entry(root)

shiba_c = ttk.Combobox(root, state = "readonly", values=['　','良','稍重','重','不良'], width = 4) #馬場状態
dirt_c = ttk.Combobox(root, state = "readonly", values=['　','良','稍重','重','不良'], width = 4)

kakutei = ttk.Combobox(root, state = "readonly", values=['　','確定','審議'], width = 4) #確定状況の設定

var_record = tk.BooleanVar()
record = tk.Checkbutton(root, text = "レコード", variable = var_record) #レコードの設定

time_min = tk.Entry(root, width = 3) #勝ちタイムの設定
time_sec = tk.Entry(root, width = 3)
time_sec10 = tk.Entry(root, width = 3)

ff_sec = tk.Entry(root, width = 3) #4Fタイムの設定
ff_sec10 = tk.Entry(root, width = 3)

tf_sec = tk.Entry(root, width = 3) #3Fタイムの設定
tf_sec10 = tk.Entry(root, width = 3)

#設定内容の反映ボタン
createbutton = tk.Button(root, text = 'create', command = createwindow)

#プログラム終了用のボタン
exitbutton = tk.Button(root, text = 'exit', command = sys.exit)

#テキストの配置
for i in range(len(labels)):
    labels[i].grid(column = 0, row = i)

#メニュー・ボックス・ボタンの配置
course.grid(column = 1, row = 0) #レース場名

race_no.grid(column = 1, row = 1) #レース番号

first_h.grid(column = 1, row = 2) #馬番の入力
second_h.grid(column = 1, row = 3)
third_h.grid(column = 1, row = 4)
fourth_h.grid(column = 1, row = 5)
fifth_h.grid(column = 1, row = 6)

margin_12.grid(column = 1, row = 7) #着差の入力
margin_23.grid(column = 1, row = 8)
margin_34.grid(column = 1, row = 9)
margin_45.grid(column = 1, row = 10)

shiba_c.grid(column = 1, row = 11) #馬場状態
dirt_c.grid(column = 1, row = 12)

kakutei.grid(column = 1, row = 13) #確定状況の設定

record.grid(column = 1, row = 14) #レコードの設定

time_min.grid(column = 1, row = 15) #勝ちタイムの設定
time_sec.grid(column = 1, row = 16)
time_sec10.grid(column = 1, row = 17)

ff_sec.grid(column = 1, row = 18) #4Fタイムの設定
ff_sec10.grid(column = 1, row = 19)

tf_sec.grid(column = 1, row = 20) #3Fタイムの設定
tf_sec10.grid(column = 1, row = 21)

createbutton.grid(column = 0, row = 22) #設定内容の反映
exitbutton.grid(column = 1, row = 22) #プログラムの終了

#ループ処理の実行
root.mainloop()