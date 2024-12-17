= 着順掲示板を作る

//abstract{
いよいよ着順掲示板の再現に入ります。
サブウィンドウの作成、ラベルの内容の変更、図形の描画と編集、place()とpack()によるウィジェットの配置について学んでいきます。
//}

#@#//makechaptitlepage[toc=on]

=={makenewwindow} 掲示板用のウィンドウを作る

ここまではひたすら設定画面を作ってきましたが、本章からは本題である掲示板の作成に入ります。

はじめに、掲示板のためのウィンドウを作成します。
前章で作成した@<code>{createwindow}関数に追記していく形で掲示板のGUIを作っていきます。

//list[newwindow][掲示板用のウィンドウを作る][indent=4]{
import tkinter as tk
from tkinter import ttk
import sys

def createwindow(): @<balloon>|掲示板を作り変える関数|
    @<del>{pass}
    @<b>|board = tk.Toplevel()|
    @<b>|board.geometry('500x850')|
    @<b>|board.resizable(False, False)|
    @<b>|board.title('掲示板')|
    @<b>|board.configure(bg='black')|
//}

既存のウィンドウからサブのウィンドウを呼び出すには、@<code>{tk.Toplevel()}を使用します。
設定画面のcreateボタンを押して掲示板ウィンドウを生成した後、
あえて右上の×ボタンを押してプログラムを終了してみてください。
@<code>{tk.Tk()}で二つ目のウィンドウを呼び出した場合、そのウィンドウは残ってしまいますが、
@<code>{tk.Toplevel()}を使用すればメインのウィンドウを消すとサブのウィンドウも消えてくれます。

@<code>{geometry},@<code>{resizable},@<code>{title}に関しては、
@<secref>{02-tuto|make-window}で紹介した内容と同様です。
その後、@<code>{configure()}に@<code>{bg}を指定し、背景色を黒にしています。
@<code>{bg}には色の名前もしくはカラーコードが指定可能です。色の指定方法に関してはこの後に登場するものも同様です。

しかし、このコードには問題があります。
お気づきだとは思いますが、この状態でcreateボタンを連打すると、
その分だけサブウィンドウを生成できてしまいます。
これを防ぐために、コードを@<list>{limitwindow}のように書き換えましょう。

//list[limitwindow][サブウィンドウの生成を制限する][indent=4]{
def createwindow(): @<balloon>|掲示板を作り変える関数|
    @<b>|global board|
    @<b>|if (board == None or not board.winfo_exists()):| @<balloon>|ウィンドウがない場合|
        board = tk.Toplevel() @<balloon>|掲示板ウィンドウの定義|
        board.geometry('500x850')
        board.resizable(False, False)
        board.title('掲示板')
        board.configure(bg='black')
    @<b>|else:| @<balloon>|ウィンドウがある場合|
        @<b>|board.destroy()| @<balloon>|ウィンドウを破棄して作り直す|
        @<b>|createwindow()|

@<b>|board = None| @<balloon>|サブウィンドウを先に定義する|
//}

サブウィンドウの生成を制限するために、@<code>{winfo_exists()}を使用しています。
この関数は、ウィンドウが存在すれば@<code>{True}を、存在しなければ@<code>{False}を返します。
返り値を@<code>{not}で反転させることによって、ウィンドウが存在しない時だけ@<code>{tk.Topleve()}を呼び出しています。

ウィンドウが存在するときは、のちに作成する図形の処理の関係でウィンドウを破棄して作り直すようにしています。

しかし、この関数はサブウィンドウが存在しているときしか利用できません。
そのため、あらかじめ@<code>{createwindow()}の外で@<code>{board}を@<code>{None}(=空っぽの状態)として定義しておき、
中のif文の条件に@<code>{None}を追加しています。
この場合、@<code>{board}は@<code>{createwindow()}関数の外で宣言された変数になるので、
関数の初めに@<code>{global board}と記述することで関数の中でも同じ変数を利用できるようにしています。

この状態でプログラムを実行し、createボタンを連打してみてください。
サブウィンドウが一つしか生成されないことが確認できるはずです。

=={placelabel} ラベルを配置する

=== 下準備

ついに掲示板の見た目の制作に入ります。
掲示板の本体は@<secref>{02-tuto|make-text}で紹介した@<code>{Label}にオプションを付け加える形で作っていきます。
これから追加していくコードのうちの一行を例として@<list>{codeexample}に示します。

//list[codeexample][これから追加するコードの例][]{
shiba_b = tk.Label(board, text='芝', font=("MSゴシック", "33", "bold"), width=2, foreground='white', bg='black')
//}

@<code>{font}は名前の通りラベルのフォントを指定します。本当は掲示板のフォントも再現したいのですが、
非常に大がかりとなってしまうのでMSゴシックの太字で代用します。@<code>{foreground}は文字の色、
@<code>{bg}はラベルの背景色です。

さて、このような設定を何度も書くことになるのですが、毎回@<code>{font=("MSゴシック", "33", "bold")}
と書くのは大変ですね。また、このプログラムのフォントはMSゴシックの太字固定で、サイズのみを変更していきます。
ということで、@<code>{("MSゴシック", "任意のサイズ", "bold")}を返す関数を作ってしまいましょう。

//list[fonteasy][フォント指定を簡略化する関数][indent=4]{
import tkinter as tk
from tkinter import ttk
import sys

#ラベルのフォントのテンプレート
@<b>|def font(size):|
@<b>|    return ("MSゴシック", str(size), "bold")|
//}

これで、@<list>{codeexample}のコードを、@<list>{codekairyo}のように簡略化することができました。

//list[codekairyo][自作したfont()を利用したフォント指定][indent=4]{
shiba_b = tk.Label(board, text='芝', font=font(33), width=2, foreground='white', bg='black')
//}

=== ラベルの宣言

前置きが長くなりましたが、ここからはラベルの宣言・配置に入ります。
一気にコードを追加していきますので、必要に応じてコピー＆ペーストを活用してください。

//list[makelabel][ラベルの宣言][indent=4]{
#掲示板を作り変える関数
def createwindow():
    global board
    if (board == None or not board.winfo_exists()):
        board = tk.Toplevel()
        board.geometry('500x850')
        board.resizable(False, False)
        board.title('掲示板')
        board.configure(bg='black')
    
    #ラベルの宣言
    #場名
    @<b>|course_b = tk.Label(board, text="\n".join(course.get()), font=font(33), foreground='white', bg='black')|
    
    #レース番号
    @<b>|race_no_b = tk.Label(board, text=race_no.get(), font=font(70), foreground='yellow', bg='black' )|
    @<b>|race_b = tk.Label(board, text='R', font=font(40), foreground='white', bg='black' )|

    #着順
    @<b>|first_b = tk.Label(board, text='Ⅰ', font=font(34), foreground='white', bg='blue')|
    @<b>|second_b = tk.Label(board, text='Ⅱ', font=font(34), foreground='white', bg='blue')|
    @<b>|third_b = tk.Label(board, text='Ⅲ', font=font(34), foreground='white', bg='blue')|
    @<b>|fourth_b = tk.Label(board, text='Ⅳ', font=font(34), foreground='white', bg='blue')|
    @<b>|fifth_b = tk.Label(board, text='Ⅴ', font=font(34), foreground='white', bg='blue')|

    #馬番
    @<b>|first_h_b = tk.Label(board, text=first_h.get(), font=font(70), width=2, foreground='yellow', bg='#707070', anchor='e')|
    @<b>|second_h_b = tk.Label(board, text=second_h.get(), font=font(70), width=2, foreground='yellow', bg='#707070', anchor='e')|
    @<b>|third_h_b = tk.Label(board, text=third_h.get(), font=font(70), width=2, foreground='yellow', bg='#707070', anchor='e')|
    @<b>|fourth_h_b = tk.Label(board, text=fourth_h.get(), font=font(70), width=2, foreground='yellow', bg='#707070', anchor='e')|
    @<b>|fifth_h_b = tk.Label(board, text=fifth_h.get(), font=font(70), width=2, foreground='yellow', bg='#707070', anchor='e')|
    
    #着差
    @<b>|margin_12_b = tk.Label(board, text=margin_12.get(), font=font(40), width=4, foreground='yellow', bg='#707070')|
    @<b>|margin_23_b = tk.Label(board, text=margin_23.get(), font=font(40), width=4, foreground='yellow', bg='#707070')|
    @<b>|margin_34_b = tk.Label(board, text=margin_34.get(), font=font(40), width=4, foreground='yellow', bg='#707070')|
    @<b>|margin_45_b = tk.Label(board, text=margin_45.get(), font=font(40), width=4, foreground='yellow', bg='#707070')|
    
    #馬場状態
    @<b>|shiba_b = tk.Label(board, text='芝', font=font(33), width=2, foreground='white', bg='black')|
    @<b>|shiba_c_b = tk.Label(board, text=shiba_c.get(), font=font(60), width=3, foreground='yellow', bg='#707070')|
    @<b>|dirt_b = tk.Label(board, text='ダート', font=font(33), foreground='white', bg='black')|
    @<b>|dirt_c_b = tk.Label(board, text=dirt_c.get(), font=font(60), width=3, foreground='yellow', bg='#707070')|

    #確定状況
    @<b>|kakutei_b = tk.Label(board, text=' ', font=font(90), width=3, foreground='white', bg='#707070')|

    #レコード
    @<b>|record_b = tk.Label(board, text=' ', font=font(45), width=4, foreground='red', bg='#707070')|

    #入線タイム
    @<b>|time_b = tk.Label(board, text='タイム', font=font(27), foreground='white', bg='black')|
    @<b>|time_min_b = tk.Label(board, text=time_min.get(), font=font(45), width=1, foreground='yellow', bg='#707070')|
    @<b>|dot = tk.Label(board, text='.', font=font(30), width=1, foreground='white', bg='black')|
    @<b>|time_sec_b = tk.Label(board, text=time_sec.get(), font=font(45), width=2, foreground='yellow', bg='#707070')|
    @<b>|dot2 = tk.Label(board, text='.', font=font(30), width=1, foreground='white', bg='black')|
    @<b>|time_sec10_b = tk.Label(board, text=time_sec10.get(), font=font(45), width=1, foreground='yellow', bg='#707070')|
    
    #4ハロン
    @<b>|ff_b = tk.Label(board, text='４Ｆ', font=font(27), foreground='white', bg='black')|
    @<b>|ff_sec_b = tk.Label(board, text=ff_sec.get(), font=font(45), width=2, foreground='yellow', bg='#707070')|
    @<b>|dot3 = tk.Label(board, text='.', font=font(30),width=1, foreground='white', bg='black')|
    @<b>|ff_sec10_b = tk.Label(board, text=ff_sec10.get(), font=font(45), width=1, foreground='yellow', bg='#707070')|
    
    #3ハロン
    @<b>|tf_b = tk.Label(board, text='３Ｆ', font=font(27), foreground='white', bg='black')|
    @<b>|tf_sec_b = tk.Label(board, text=tf_sec.get(), font=font(45), width=2, foreground='yellow', bg='#707070')|
    @<b>|dot4 = tk.Label(board,text='.', font=font(30), width=1, foreground='white', bg='black')|
    @<b>|tf_sec10_b = tk.Label(board, text=tf_sec10.get(), font=font(45), width=1, foreground='yellow', bg='#707070')|
//}

下準備の際に解説していないオプションについて解説していきます。
@<code>{anchor}は、ラベルの文字列の寄せ方を指定します。
着順掲示板の馬番は右寄せの配置なので、@<code>{e}を指定しています。
他にも、@<code>{w}(左寄せ)、@<code>{n}(上寄せ)、@<code>{s}(下寄せ)などの寄せ方が用意されています。

一部のLabelにおいて、テキストに@<code>{get()}関数を指定しています。
これは、Entryをはじめとした文字列を入力もしくは指定できるウィジェットの内容を取得する関数です。

4ハロン、3ハロンのラベルにおいて、4F、3Fが全角になっていますが、こちらは意図的に全角にしています。

=== ラベルの配置

それでは、宣言したラベルを配置していきます！
こちらも記述量が多いですが、頑張って書いていきましょう。

//list[labelplace][ラベルの配置][indent=4]{
#掲示板を作り変える関数
def createwindow():
    ...(省略)...
    tf_sec10_b = tk.Label(board, text=tf_sec10.get(), font=font(45), width=1, foreground='yellow', bg='#707070')

    #ラベルの配置
    @<b>|course_b.place(x=20, y=10) #場名|
    
    @<b>|race_b.place(x=150, y=35) #R|
    
    @<b>|first_b.place(x=24, y=132) #着順|
    @<b>|second_b.place(x=24, y=222)|
    @<b>|third_b.place(x=24, y=312)|
    @<b>|fourth_b.place(x=24, y=402)|
    @<b>|fifth_b.place(x=24, y=492)|
    
    @<b>|first_h_b.place(x=100, y=125, height=72) #馬番|
    @<b>|second_h_b.place(x=100, y=215, height=72)|
    @<b>|third_h_b.place(x=100, y=305, height=72)|
    @<b>|fourth_h_b.place(x=100, y=395, height=72)|
    @<b>|fifth_h_b.place(x=100, y=485, height=72)|
    
    @<b>|margin_12_b.place(x=310, y=165, height=60) #着差|
    @<b>|margin_23_b.place(x=310, y=260, height=60)|
    @<b>|margin_34_b.place(x=310, y=355, height=60)|
    @<b>|margin_45_b.place(x=310, y=450, height=60)|
    
    @<b>|shiba_b.place(x=60, y=560) #馬場状態|
    @<b>|shiba_c_b.place(x=15, y=610, height=75)|
    @<b>|dirt_b.place(x=22, y=700)|
    @<b>|dirt_c_b.place(x=15, y=750, height=75)|
    
    @<b>|kakutei_b.place(x=250 , y=10, height=120) #確定状況|

    @<b>|record_b.place(x=290, y=550, height=55) #レコード|
    
    @<b>|time_b.place(x=170, y=645) #入線タイム|
    @<b>|time_min_b.place(x=283, y=630, height=55)|
    @<b>|dot.place(x=323, y=623, height=100)|
    @<b>|time_sec_b.place(x=350, y=630, height=55)|
    @<b>|dot2.place(x=425, y=623, height=100)|
    @<b>|time_sec10_b.place(x=452, y=630,height=55)|

    @<b>|ff_b.place(x=205, y=715) #4ハロン|
    @<b>|ff_sec_b.place(x=350, y=700, height=55)|
    @<b>|dot3.place(x=425, y=693, height=100)|
    @<b>|ff_sec10_b.place(x=452, y=700, height=55)|
    
    @<b>|tf_b.place(x=205, y=780) #3ハロン|
    @<b>|tf_sec_b.place(x=350, y=770, height=55)|
    @<b>|dot4.place(x=425, y=770, height=78)|
    @<b>|tf_sec10_b.place(x=452, y=770, height=55)|
//}

ここで、新たなウィジェットの配置方法として@<code>{place()}が登場します。
これは、ウィンドウ(配置先)の左上を原点として、座標を指定してウィジェットを配置する関数です。
@<code>{x}でx座標、@<code>{y}でy座標を指定しています。
@<code>{relx, rely}を使用すると相対指定による配置もできますが、
今回はウィンドウの大きさの変更を禁止しているので、絶対指定で配置します。

一部のウィジェットは@<code>{height}で高さ(縦の幅)を指定しています。

ここで、いったんプログラムを実行し、設定画面のcreateボタンを押して掲示板の見た目を確認してみましょう。
@<img>{board1}のように表示されていれば大丈夫です。一気に華やかになりましたね。

//image[board1][現時点での掲示板][border=on]

=== テキスト部分を完成させる

==== レース番号の見た目を変える

見た目はほとんど完成しましたが、レース番号、確定状況、レコードの表示がまだ不十分なので仕上げていきます。
はじめに、レース番号の見た目を完成させましょう。競馬場で使用されている掲示板は、レース番号を範囲いっぱいに表示しています。
そのため、1~9レースまでと、10~12レースで、フォントのサイズを変えていきます。

//list[raceno][レース番号の見た目][indent=4]{
    #レース番号
    @<del>|race_no_b = tk.Label(board, text=race_no.get(), font=font(70), foreground='yellow', bg='black' )|
@<b>|   if (len(number := race_no.get()) == 2):|
@<b>|        race_no_b = tk.Label(board, text=number, font=font(50), width=2, foreground='yellow', bg='black' )|
@<b>|        race_no_b.place(x=65, y=23)|
@<b>|    else:|
@<b>|        race_no_b = tk.Label(board, text=number, font=font(70), width=2, foreground='yellow', bg='black' )|
@<b>|        race_no_b.place(x=65, y=8)|
@<b>|    race_b = tk.Label(board, text='R', font=font(40), foreground='white', bg='black' )|
//}

@<code>{len()}関数で条件分岐させ、フォントサイズを変更しています。
また、ウィジェットを配置する位置も少し変更しています。

ここで見慣れない演算子@<code>{:=}が登場していますね。これはセイウチ演算子と呼ばれるもので、
条件式内で変数への代入処理を可能にします。C言語ではファイルの読み書きで頻出の処理ですね。
Pythonでそれを行うにはこのように特殊な演算子を使う必要があります。

プログラムを実行し、@<img>{racemitame}のように1~9レースまでと10~12レースでフォントのサイズが変わるか確かめましょう。
スピンボックスの内容を変える度にcreateボタンを押す必要があることに注意してください。

//image[racemitame][レース番号の動作テスト][border=on]

==== 確定状況を完成させる

掲示板の右上に表示される@<B>{確定}、@<B>{審議}の文字は、背景色も変化します。
そのため先ほどの項ではあえて完成させず、ここで改めて完成させます。

//list[kakutei][確定状況の完成][indent=4]{
    #確定状況
    @<del>|kakutei_b = tk.Label(board, text=' ', font=font(90), width=3, foreground='white', bg='#707070')|
    @<b>|if ((text := kakutei.get()) == '確定'):|
    @<b>|    kakutei_b = tk.Label(board, text=text, font=font(90), width=3, foreground='white', bg='red')|
    @<b>|elif (text == '審議'):|
    @<b>|    kakutei_b = tk.Label(board, text=text, font=font(90), width=3, foreground='white', bg='blue')|
    @<b>|else:|
    @<b>|    kakutei_b = tk.Label(board, text=' ', font=font(90), width=3, foreground='white', bg='#707070')|
//}

プルダウンメニューで@<B>{確定}が選択された場合は背景を赤に、@<B>{審議}が選択された場合は背景を青に、
何も選択されていないときは背景をグレーにしています。

こちらもプログラムを実行し、@<img>{kakuteimitame}のようにテキストと背景色が変更されるか確認しましょう。

//image[kakuteimitame][確定状況の動作テスト][border=on]

==== レコードの表示を完成させる

長かったこの節もこれで最後です。レコードの表示を完成させましょう。

//list[record][レコード表示の完成][indent=4]{
    #レコード
    @<del>|record_b = tk.Label(board, text=' ', font=font(45), width=4, foreground='red', bg='#707070')|
    @<b>|if var_record.get():|
        @<b>|record_b = tk.Label(board, text='ﾚｺｰﾄﾞ', font=font(45), width=4, foreground='red', bg='#707070')|
    @<b>|else:|
        @<b>|record_b = tk.Label(board, text='', font=font(45), width=4, foreground='red', bg='#707070')|
//}

先ほどまでと同様に条件分岐でテキストの内容を変更しています。
判定用の変数にはチェックボックスを作成するときに@<code>{variable}に指定したものを使います。
@<secref>{03-configwindow|checkbox}で解説したように、これは二値変数なので、条件式はとても単純です。

プログラムを実行し、@<img>{recordmitame}のようにチェックを付け外しして見た目が変わるか確認しましょう。

//image[recordmitame][レコードの動作テスト][border=on]

これで、設定画面の入力内容の反映が全て終わりました！一度、実際のレースの結果を入力して動作を確認します。
2022年の日本ダービー(勝ち馬:ドウデュース)を再現してみます。

//image[minitest][現時点での完成図][border=on]

=={makecanvas} 図形を作成する

掲示板の機能はほとんど完成しましたが、まだ見た目が異なる部分が存在します。
着順のローマ数字の背景が四角になっていますね。ということで、図形の描画を使って背景を丸に変更します。

//list[canvas][canvasの宣言][indent=4]{
#掲示板を作り変える関数
def createwindow():
    global board
    if (board == None or not board.winfo_exists()):
        board = tk.Toplevel()
        board.geometry('500x850')
        board.resizable(False, False)
        board.title('掲示板')
        board.configure(bg='black')
    
    @<b>|canvas = tk.Canvas(board, bg='black', height=850, width=510 )|
//}

図形の描画には@<code>{canvas}を使用します。
ここまでのウィジェットは全てウィンドウに配置していましたが、図形はキャンバスを作り、その上に配置していきます。

キャンバスを作成出来たら、円を作成していきましょう。

//list[placecircle][円の配置][indent=4]{
    tf_sec10_b = tk.Label(board, text=tf_sec10.get(), font=font(45), width=1, foreground='yellow', bg='#707070')

    #着順の後ろに表示する円
    @<b>|canvas.create_oval(10, 120, 90, 200, fill='blue')|
    @<b>|canvas.create_oval(10, 210, 90, 290, fill='blue')|
    @<b>|canvas.create_oval(10, 300, 90, 380, fill='blue')|
    @<b>|canvas.create_oval(10, 390, 90, 470, fill='blue')|
    @<b>|canvas.create_oval(10, 480, 90, 560, fill='blue')|

    #円を配置
    @<b>|canvas.pack()|
//}

円の作成には、@<code>{create_oval()}を使用します。名前の通り、円だけでなく楕円も作成することができます。
最初の二つの引数は始点のx座標とy座標、三つ目と四つ目の引数は対角点のx座標とy座標に対応しています。
@<code>{fill}で円の色を指定しています。指定の方法についてはこれまでと同様です。

プログラムを実行してみましょう。@<img>{circle}のようになっていれば成功です。

//image[circle][円の作成][border=on]

=={doutyaku} 同着の処理を作る

これで完成・・・と言いたいところですが、実は忘れている機能があります。
実は、同着が発生した場合、着順のローマ数字が変化するようになっています。

ということで、その処理を作成していきましょう。

//list[makedotyaku][同着処理の追加][indent=4]{
    tf_sec10_b.place(x=452, y=770, height=55)

    @<b>|same = 0 #判定用の変数|
    #同着処理
    @<b>|if margin_12.get() == '同着': #1着同着の場合|
    @<b>|    second_b.configure(text='Ⅰ')|
    @<b>|    same = 1|

    @<b>|if margin_23.get() == '同着': #2着同着の場合|
    @<b>|    if same == 1:|
    @<b>|        third_b.configure(text='Ⅰ') #1~3着同着の場合|
    @<b>|    else:|
    @<b>|        third_b.configure(text='Ⅱ')|
    @<b>|        same = 2|
    @<b>|else:|
        @<b>|same = 3|

    @<b>|if margin_34.get() == '同着': #3着同着の場合|
    @<b>|    if same == 1:|
    @<b>|        fourth_b.configure(text='Ⅰ') #1~4着同着の場合|
    @<b>|    elif same == 2:|
    @<b>|        fourth_b.configure(text='Ⅱ') #2~4着同着の場合|
    @<b>|    else:|
    @<b>|        fourth_b.configure(text='Ⅲ')|
    @<b>|        same = 3|
    @<b>|else:|
        @<b>|same = 4|

    @<b>|if margin_45.get() == '同着': #4着同着の場合|
    @<b>|    if same == 1:|
    @<b>|        fifth_b.configure(text='Ⅰ') #1~5着同着の場合|
    @<b>|    elif same == 2:|
    @<b>|        fifth_b.configure(text='Ⅱ') #2~5着同着の場合|
    @<b>|    elif same == 3:|
    @<b>|        fifth_b.configure(text='Ⅲ') #3~5着同着の場合|
    @<b>|    else:|
    @<b>|        fifth_b.configure(text='Ⅳ')|
//}

着差に@<B>{同着}と書かれたときに、条件式が働きます。
ボックスの文字の取得とその判定を何度も行わないために、判定用の変数を導入しています。
若干コードは長くなりますが、何度も同着と書くよりは楽だと思います。

ここで、新しい関数@<code>{configure}が登場しています。
これは、ウィジェットに対して操作を行う関数です。
ここではラベルのテキストの内容を変更するために使用しています。

プログラムを実行し、好きな着差の欄に@<B>{同着}と書き込んでみましょう。
書き込んでみた例を@<img>{doutyaku}に示します。パターンが多すぎるので一つの例しか紹介できませんが、
どのパターンでも正常に動作するはずです。

//image[doutyaku][同着判定の動作の様子][border=on]