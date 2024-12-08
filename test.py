import tkinter as tk
from tkinter import ttk
import sys

#掲示板を作り変える関数
def createwindow():
    pass

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

shiba_c = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4) #馬場状態
dirt_c = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)

kakutei = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4) #確定状況の設定

record = tk.Checkbutton(root, text="レコード") #レコードの設定

time_min = tk.Spinbox(root, from_ = 0, to = 9, width = 3) #勝ちタイムの設定
time_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3)
time_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)

ff_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3) #4Fタイムの設定
ff_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)

tf_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3) #3Fタイムの設定
tf_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)

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