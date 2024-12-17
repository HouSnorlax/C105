= チュートリアル

//abstract{
ウィンドウの作成、ラベルの配置について学んでいきます。
//}

#@#//makechaptitlepage[toc=on]

=={compimage} 完成イメージ
プログラムを書き始める前に、完成イメージを示しておきます。
このプログラムは、の設定画面と、の掲示板部分の二つのウィンドウで構成されます。

電光掲示板は競馬場によって微妙に違いがあるのですが、
今回は東京競馬場で使用されているものを参考に作成していきます。


=={make-window} ウィンドウの作成

それではプログラムを書いていきましょう。
はじめに、Pythonのファイルを作成し、@<list>{win1}に示すコードを書き込んでください。
本書のプログラムは、このファイルのみで完結します。

//list[win1][arrivalboard.py]{
import tkinter as tk @<balloon>{Tkinterモジュールの読み込み}

root = tk.Tk() @<balloon>{インスタンスの作成}

root.geometry('225x500')@<balloon>{ウィンドウを作成}
root.resizable(False, False)
root.title('設定画面')

root.mainloop()@<balloon>{ループ処理の実行}
//}

はじめに、Tkinterのライブラリをインポートします。
今後、Tkinterの関数を何度も使うことになりますが、その度に@<code>{tkinter}と書くのは面倒なので、
@<code>{as}を利用して@<code>{tk}という名前でインポートしています。

次に、Tkクラスのインスタンスを作成します。
いきなり何を言っているんだという感じですが、クラスとインスタンスに関する解説をすると、
初心者向けの範囲を逸脱してしまうので、ここでは省略いたします。
ここではおまじないとして見ていただいて構いません。

続いて、ウィンドウの設定をしていきます。@<code>{geometry()}でウィンドウのサイズを設定し、
@<code>{resizable()}でサイズの変更を禁止しています。二つのFalseはそれぞれ横方向と縦方向に対応しています。
最後に@<code>{title()}でタイトルを設定します。このウィンドウはのちに掲示板の表示内容を設定するために使うので、
名前を「設定画面」としておきます。

最後に、@<code>{mainloop()}によって、待機状態に入ります。
この文を忘れると、プログラムを実行した直後にウィンドウが消えてしまいます。
また、この文の後に書かれたコードはウィンドウが消えるまで実行されません。

それでは、プログラムを実行してみましょう。

//terminal[exe1][プログラムの実行]{
$ @<userinput>{python3 arrivalboard.py}
//}

プログラムを実行すると、@<img>{window1}のように、サイズを変更できないウィンドウのみが表示されるはずです。
×ボタンを押すとウィンドウが閉じられ、プログラムの実行も終了します。

//image[window1][実行結果][border=on]

//clearpage

=={make-text} ラベルの配置

次に、ラベルを配置してみます。
ラベルは、テキストや画像を表示するための部品で、Tkinterの基本的なものになります。
先ほど作成したプログラムに、@<list>{text1}のようにコードを追加します。

ここで追加するラベルは、次章以降で追加していく要素の下準備を兼ねています。

//list[text1][ラベルの配置]{
import tkinter as tk @<balloon>{Tkinterモジュールの読み込み}

root = tk.Tk() @<balloon>{インスタンスの作成}

root.geometry('225x500')@<balloon>{ウィンドウを作成}
root.resizable(False, False)
root.title('設定画面')

@<b>{joumei = tk.Label(root, text='場名')} @<balloon>{ラベルの設定:レース場名}

@<b>{joumei.grid(column=0, row=0)} @<balloon>{ラベルの配置}

root.mainloop() @<balloon>{ループ処理の実行}
//}

ラベルを配置する際は、@<code>{Label()}を使用します。
ここでは第一引数にラベルを配置するウィンドウを、第二引数にはテキストの内容を代入しています。
さらに細かい設定をすることができますが、その説明はこの章では行いません。

ラベルは宣言しただけでは表示されず、配置をしてようやく表示されます。
これはほかの部品(ウィジェットと呼びます)についても同じことが言えます。
ここでは、@<code>{grid()}を使用して配置します。
@<code>{grid()}はウィンドウを行と列に分けて、ウィジェットを格子状に配置します。

ウィジェットを配置する方法として、他に@<code>{place()}と@<code>{pack()}がありますが、
この二つはのちほど紹介します。

コードを追加し終わったら、@<list>{exe1}のコマンドでプログラムを実行しましょう。
@<img>{window2}のように表示されれば成功です。
後にウィジェットを追加する都合上とても寂しい見た目になっていますが、これでラベルの配置ができました。

//image[window2][ラベルを配置した結果][border=on]

//clearpage

=={shita} 次の章に向けての下準備

次の章では、メニュー、ボックス、ボタンの作成方法を学んでいきます。
その前に、あらかじめラベルを配置しておきましょう。
プログラムを次のように変更していくわけですが……

//list[text2][ラベルの追加]{
joumei = tk.Label(root, text='場名') @<balloon>{ラベルの設定:レース場名}
@<b>{raceno = tk.Label(root, text='R')} @<balloon>{レース番号}
@<b>{first_p =tk.Label(root, text='1着馬')} @<balloon>{n着馬}
@<b>{second_p =tk.Label(root, text='2着馬')}
@<b>{third_p =tk.Label(root, text='3着馬')}
@<b>{fourth_p =tk.Label(root, text='4着馬')}
@<b>{fifth_p =tk.Label(root, text='5着馬')}

joumei.grid(column=0, row=0) @<balloon>{ラベルの配置}
@<b>{raceno.grid(column=0, row=1)}
@<b>{first_p.grid(column=0, row=2)}
@<b>{second_p.grid(column=0, row=3)}
@<b>{third_p.grid(column=0, row=4)}
@<b>{fourth_p.grid(column=0, row=5)}
@<b>{fifth_p.grid(column=0, row=6)}
//}

似たようなコードが繰り返されていて無駄が多いですね。
ということで、@<list>{text3}のように変更してしまいます。

//list[text3][ラベルの追加（変更版）][indent=4]{
@<b>{labels = []} @<balloon>{設定画面のラベル用配列}

@<del>{joumei = tk.Label(root, text='場名')} @<balloon>{ラベルの設定:レース場名}
@<del>{raceno = tk.Label(root, text='R')} @<balloon>{レース番号}
@<del>{first_p =tk.Label(root, text='1着馬')} @<balloon>{n着馬}
@<del>{second_p =tk.Label(root, text='2着馬')}
@<del>{third_p =tk.Label(root, text='3着馬')}
@<del>{fourth_p =tk.Label(root, text='4着馬')}
@<del>{fifth_p =tk.Label(root, text='5着馬')}
@<b>{labels.append(tk.Label(root, text='場名'))} @<balloon>{ラベルの設定:レース場名}
@<b>{labels.append(tk.Label(root, text='R'))} @<balloon>{レース番号}

@<b>{for i in range(1,6):}
@<b>{    labels.append(tk.Label(root, text=str(i) + "着馬"))} @<balloon>{n着馬}

@<del>{joumei.grid(column=0, row=0)} @<balloon>{ラベルの配置}
@<del>{raceno.grid(column=0, row=1)}
@<del>{first_p.grid(column=0, row=2)}
@<del>{second_p.grid(column=0, row=3)}
@<del>{third_p.grid(column=0, row=4)}
@<del>{fourth_p.grid(column=0, row=5)}
@<del>{fifth_p.grid(column=0, row=6)}
@<b>{for i in range(len(labels)):}
@<b>{    labels[i].grid(column=0, row=i)}
//}

この状態のプログラムを実行してみます。ラベルを配列にまとめても、ラベルを配置できることがわかります。
これで、大幅に無駄を削減できました。

しかし、これはプログラムの完成形が決まっており、
かつ後からラベルの内容を変更したり、別の箇所で呼び出したりしないためにできることであって、
どのような場面でも効果的に活用できる方法ではないことに留意が必要です。
第3章以降では、この方法は使用しません。

残りのラベルも配置していきます。

//list[text4][残りのラベルの追加][indent=4]{
labels.append(tk.Label(root, text='場名')) @<balloon>{ラベルの設定:レース場名}
labels.append(tk.Label(root, text='R'))  @<balloon>{レース番号}

for i in range(1,6):
    labels.append(tk.Label(root, text=str(i) + "着馬")) @<balloon>{n着馬}

@<b>{for i in range(1,5):}
@<b>{    labels.append(tk.Label(root, text='着差' + str(i) + "," + str(i+1)))} @<balloon>{着差}

@<b>{labels.append(tk.Label(root, text='芝'))} @<balloon>{馬場状態}
@<b>{labels.append(tk.Label(root, text='ダート'))}

@<b>{labels.append(tk.Label(root, text='状況'))} @<balloon>{確定状況}
@<b>{abels.append(tk.Label(root, text='レコード')) }

@<b>{labels.append(tk.Label(root, text='time min.'))} @<balloon>{入線タイム}
@<b>{labels.append(tk.Label(root, text='time sec'))}
@<b>{labels.append(tk.Label(root, text='time 1/10'))}

@<b>{labels.append(tk.Label(root, text='4F sec'))} @<balloon>{4ハロン}
@<b>{labels.append(tk.Label(root, text='4F 1/10 sec'))}

@<b>{labels.append(tk.Label(root, text='3F sec'))} @<balloon>{3ハロン}
@<b>{labels.append(tk.Label(root, text='3F 1/10 sec'))}

for i in range(len(labels)): @<balloon>{ラベルの配置}
    labels[i].grid(column=0, row=i)
//}

これでこの章の内容は終わりです。プログラムを実行した際に@<img>{window4}のようになっていればOKです。

//image[window4][2章の完成形][border=on]