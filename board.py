import tkinter
import sys
from tkinter import ttk

def createwindow():
    joumei.configure(text = "\n".join(box1.get()))
    if (box2.get() == '10') or (box2.get() == '11') or (box2.get() == '12'):
        race1.configure(text = box2.get(),font=("MSゴシック", "50", "bold"))
        race1.place(x = 75, y = 23)
    else:
        race1.configure(text = box2.get(),font=("MSゴシック", "70", "bold"))
        race1.place(x = 80, y = 11)
    first_h.configure(text = box3.get())
    second_h.configure(text = box4.get())
    third_h.configure(text = box5.get())
    fourth_h.configure(text = box6.get())
    fifth_h.configure(text = box7.get())
    siba2.configure(text = box12.get())
    dirt2.configure(text = box13.get())
    if box14.get() == '確定':
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = 'red')
    elif box14.get() == '審議':
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = 'blue')
    else:
        now.configure(text = box14.get(), font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = '#696969')

#ウィンドウ作成
root = tkinter.Tk()
root2 = tkinter.Tk()
root.geometry('250x450')
root2.geometry('500x850')
root2.configure(bg = 'black')
root.title('設定画面')
root2.title('掲示板')
canvas = tkinter.Canvas(root2, bg = 'black', height = 900, width = 500 )

#rootの内容
label1 = tkinter.Label(root, text = '場名')
box1 = ttk.Combobox(root,  values=['　　','東京','中山','阪神','京都','中京','小倉','新潟','福島','札幌','函館'], width = 4)
box１.current(0)
label2 = tkinter.Label(root, text = 'R')
box2 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12], width = 2)
box2.current(0)
label3 =tkinter.Label(root, text = '1')
box3 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
box3.current(0)
label4 = tkinter.Label(root, text = '2')
box4 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
box4.current(0)
label5 = tkinter.Label(root, text = '3')
box5 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
box5.current(0)
label6 = tkinter.Label(root, text = '4')
box6 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
box6.current(0)
label7 = tkinter.Label(root, text = '5')
box7 = ttk.Combobox(root, state="readonly", values=[' ',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], width = 2)
box7.current(0)
createbutton = tkinter.Button(root, text = 'create' ,command = createwindow)
exitbutton = tkinter.Button(root, text = 'exit' , command = sys.exit)
label8 =tkinter.Label(root, text = '1,2')
box8 = tkinter.Entry(root)
label9 =tkinter.Label(root, text = '2,3')
box9 = tkinter.Entry(root)
label10 =tkinter.Label(root, text = '3,4')
box10 = tkinter.Entry(root)
label11 =tkinter.Label(root, text = '4,5')
box11 = tkinter.Entry(root)
label12 = tkinter.Label(root, text = '芝')
box12 = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)
box12.current(0)
label13 = tkinter.Label(root, text = 'ダート')
box13 = ttk.Combobox(root, state="readonly", values=['　','良','稍重','重','不良'], width = 4)
box13.current(0)
label14 = tkinter.Label(root, text = '状況')
box14 = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4)
box14.current(0)

#root2の内容
joumei = tkinter.Label(root2,text="\n".join('　　'), font=("MSゴシック", "33", "bold"), foreground = 'white', bg = 'black')
race1 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), foreground = 'yellow', bg = 'black' )
race2 = tkinter.Label(root2,text = 'R', font=("MSゴシック", "40", "bold"), foreground = 'white', bg = 'black' )
first = tkinter.Label(root2,text = 'Ⅰ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
second = tkinter.Label(root2,text = 'Ⅱ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
third = tkinter.Label(root2,text = 'Ⅲ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fourth = tkinter.Label(root2,text = 'Ⅳ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
fifth = tkinter.Label(root2,text = 'Ⅴ', font=("MSゴシック", "34", "bold"), foreground = 'white' ,bg = 'blue')
first_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
second_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
third_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fourth_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
fifth_h = tkinter.Label(root2,text = ' ', font=("MSゴシック", "70", "bold"), width = 2,foreground = 'yellow' ,bg = '#696969', anchor = 'e')
siba1 = tkinter.Label(root2,text = '芝', font=("MSゴシック", "33", "bold"), width = 2,foreground = 'white' ,bg = 'black')
siba2 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
dirt1 = tkinter.Label(root2,text = 'ダート', font=("MSゴシック", "33", "bold"), foreground = 'white' ,bg = 'black')
dirt2 = tkinter.Label(root2,text = ' ', font=("MSゴシック", "60", "bold"), width = 3,foreground = 'yellow' ,bg = '#696969', anchor = 'center')
now = tkinter.Label(root2,text = ' ', font=("MSゴシック", "90", "bold"), width = 3,foreground = 'white' ,bg = '#696969')

#canvasの内容
canvas.create_oval(10,120,90,200,fill = 'blue')
canvas.create_oval(10,210,90,290,fill = 'blue')
canvas.create_oval(10,300,90,380,fill = 'blue')
canvas.create_oval(10,390,90,470,fill = 'blue')
canvas.create_oval(10,480,90,560,fill = 'blue')


#canvas pack
canvas.pack()

#root grid
label1.grid(column = 0 ,row = 0, padx = [10,10])
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
createbutton.grid(column = 0, row = 14)
exitbutton.grid(column = 1, row = 14)

#root2 place
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
#実行
root.mainloop()
root2.mainloop()