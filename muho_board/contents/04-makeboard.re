= 着順掲示板を作る

//abstract{
いよいよ着順掲示板の再現に入ります。
サブウィンドウの作成、ラベルの内容の変更、図形の描画、place()とpack()について学んでいきます。
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

#掲示板を作り変える関数
def createwindow():
    @<del>{pass}
    @<b>|board = tk.Toplevel()|
    @<b>|board.geometry('500x850')|
    @<b>|board.resizable(False, False)|
    @<b>|board.title('掲示板')|
    @<b>|board.configure(bg = 'black')|
//}

既存のウィンドウからサブのウィンドウを呼び出すには、@<code>{tk.Toplevel()}を使用します。
設定画面のcreateボタンを押して掲示板ウィンドウを生成した後、
あえて右上の×ボタンを押してプログラムを終了してみてください。
@<code>{tk.Tk()}で二つ目のウィンドウを呼び出した場合、そのウィンドウは残ってしまいますが、
@<code>{tk.Toplevel()}を使用すればメインのウィンドウを消すとサブのウィンドウも消えてくれます。

@<code>{geometry},@<code>{resizable},@<code>{title}に関しては、
@<chap>{02-tuto}のはじめに紹介した内容と同様です。
その後、@<code>{configure()}で背景色を黒にしています。

しかし、このコードには問題があります。
お気づきだとは思いますが、この状態でcreateボタンを連打すると、
その分だけサブウィンドウを生成できてしまいます。
これを防ぐために、コードを@<list>{limitwindow}のように書き換えましょう。

//list[limitwindow][サブウィンドウの生成を制限する][indent=4]{
#掲示板を作り変える関数
def createwindow():
    @<b>|global board|
    @<b>|if (board == None or not board.winfo_exists()):|
        board = tk.Toplevel()
        board.geometry('500x850')
        board.resizable(False, False)
        board.title('掲示板')
        board.configure(bg = 'black')

#サブウィンドウを先に定義する
@<b>|board = None|
//}

サブウィンドウの生成を制限するために、@<code>{winfo_exists()}を使用しています。
この関数は、ウィンドウが存在すればTrueを、存在しなければFalseを返します。
返り値をnotで反転させることによって、ウィンドウが存在しない時だけ@<code>{tk.Topleve()}を呼び出しています。

しかし、この関数はサブウィンドウが存在しているときしか利用できません。
そのため、あらかじめ@<code>{createwindow()}の外で@<code>{board}を@<code>{None}(=空っぽの状態)として定義しておき、
中のif文の条件に@<code>{None}を追加しています。
この場合、@<code>{board}は@<code>{createwindow()}関数の外で宣言された変数になるので、
関数の初めに@<code>{global board}と記述することで関数の中でも同じ変数を利用できるようにしています。

この状態でプログラムを実行し、createボタンを連打してみてください。
サブウィンドウが一つしか生成されないことが確認できるはずです。

=={placelabel} ラベルを配置する

あ