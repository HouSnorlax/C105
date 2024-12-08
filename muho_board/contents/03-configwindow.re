= 設定画面を完成させる

//abstract{
メニュー、ボックス、ボタンの作成方法を学んでいきます。
//}

#@#//makechaptitlepage[toc=on]

=={textbox} テキストボックス

テキストボックスとは、ユーザーが任意の文字を入力できるウィジェットです。
ここでは、着差の入力に使用します。

//list[tbox][テキストボックスの作成][indent=4]{
labels.append(tk.Label(root, text = '3F 1/10'))

#メニュー・ボックス・ボタンの作成
@<b>|margin_12 = tk.Entry(root) #着差の入力|
@<b>|margin_23 = tk.Entry(root)|
@<b>|margin_34 = tk.Entry(root)|
@<b>|margin_45 = tk.Entry(root)|

#テキストの配置
for i in range(len(labels)):
    labels[i].grid(column = 0, row = i)

#メニュー・ボックス・ボタンの配置
@<b>|margin_12.grid(column = 1, row = 7) #着差の入力|
@<b>|margin_23.grid(column = 1, row = 8)|
@<b>|margin_34.grid(column = 1, row = 9)|
@<b>|margin_45.grid(column = 1, row = 10)|
//}

いきなりrow=7となっていますが、ここからは解説の都合でウィジェットの作成順が画面での並びと一致しません。
ご了承ください。

テキストボックスの作成には、@<code>{Entry()}を使用します。
引数として表示させたいウィンドウを渡しています。とても単純ですね。

プログラムを実行し、@<img>{margintext}のように表示されていれば成功です。

//image[margintext][作成したテキストボックス][border=on]

=={pulldown} プルダウンメニュー

プルダウンメニューとは、あらかじめ用意されたリストから項目を選択できるウィジェットです。
@<img>{pulldownmenu}のように、場名の選択メニューを作りながら、作成方法を解説します。

さっそくコードを書いていきましょう。@<list>{pdown}のプログラムを追加してください。

//image[pulldownmenu][プルダウンメニュー][border=on]

//list[pdown][プルダウンメニューの作成][indent=4]{
import tkinter as tk
@<b>{from tkinter import ttk}

...(省略)...
#メニュー・ボックス・ボタンの配置
@<b>|course = ttk.Combobox(root,  values=['　　','札幌','函館','福島','新潟','中山','東京','中京','京都','阪神','小倉'], width = 4)| #レース場名

margin_12.grid(column = 1, row = 7) #着差の入力

...(省略)...

#メニュー・ボックス・ボタンの配置
@<b>|course.grid(column = 1, row = 0) #レース場名 |

margin_12.grid(column = 1, row = 7) #着差の入力
//}

ここで、ttkという新たなモジュールをインポートしています。
より機能が充実したTKinterという風に思っていただければ大丈夫です。

また、tkと非常に似ているのでプログラムのミスに注意してください。
あまりにも紛らわしいのであれば一行目の@<code>{as tk}を削除したり(プログラム中の@<code>{tk}を全て修正することになります)、
ttkを別の名前でインポートしても構いません。

プルダウンメニューの作成には、@<code>{ttk.Combobox()}を使用します。
@<code>{values}にリストを代入すると、その要素がそのまま選択肢になります。

@<code>{width}は名前の通り、メニューの幅を指定することができます。
選択肢にある競馬場はすべて漢字二文字なので、幅は4に設定しておきます。

また、メニューの下三角以外の部分をクリックすると、直接文字を入力することができます。
本書では中央競馬の掲示板の再現を目的としているので、選択肢には中央競馬場のみ用意しましたが、
地方競馬や廃止となってしまった競馬場の名前を入力して楽しむこともできます。

ここでおことわりなのですが、今回作成する掲示板はレイアウトの都合上三文字の競馬場に対応していません。
名古屋競馬ファンの皆様、ごめんなさい・・・

==== 直接の入力を禁止する

しかし、なんでもかんでも入力されてしまうと困る場面もあります。
引数の中に@<code>{state="readonly"}と追加することで、プルダウンメニューを読み取り専用にできます。

//list[denyinput][入力の禁止][indent=4]{
#メニュー・ボックス・ボタンの作成
...(省略)...
margin_45 = tk.Entry(root)

@<b>|shiba_c = ttk.Combobox(root, state = "readonly", values=['　','良','稍重','重','不良'], width = 4) #馬場状態|
@<b>|dirt_c = ttk.Combobox(root, state = "readonly", values=['　','良','稍重','重','不良'], width = 4)|

@<b>|kakutei = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4) #確定状況の設定|

...(省略)...

#メニュー・ボックス・ボタンの配置
...(省略)...
margin_45.grid(column = 1, row = 10)

@<b>|shiba_c.grid(column = 1, row = 11) #馬場状態|
@<b>|dirt_c.grid(column = 1, row = 12)|

@<b>|kakutei.grid(column = 1, row = 13) #確定状況の設定|
//}

=={spinbox} スピンボックス

スピンボックスとは、数値を入力するためのテキストボックスです。
数値を直接入力できるほかに、上下の三角ボタンを使って数値を増減させることもできます。

//list[spinb][スピンボックスの作成][indent=4]{
#メニュー・ボックス・ボタンの作成
course = ttk.Combobox(root,  values=['　　','札幌','函館','福島','新潟','中山','東京','中京','京都','阪神','小倉'], width = 4) #レース場名

@<b>|race_no = tk.Spinbox(root, from_ = 1, to = 12, width = 3) #レース番号|

@<b>|first_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) #馬番の入力|
@<b>|second_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) |
@<b>|third_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) |
@<b>|fourth_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3) |
@<b>|fifth_h = tk.Spinbox(root, from_ = 1, to = 18, width = 3)|

...(省略)...

#メニュー・ボックス・ボタンの配置
course.grid(column = 1, row = 0) #レース場名

@<b>|race_no.grid(column = 1, row = 1) #レース番号|

@<b>|first_h.grid(column = 1, row = 2) #馬番の入力|
@<b>|second_h.grid(column = 1, row = 3)|
@<b>|third_h.grid(column = 1, row = 4)|
@<b>|fourth_h.grid(column = 1, row = 5)|
@<b>|fifth_h.grid(column = 1, row = 6)|
//}

スピンボックスの作成には、@<code>{Spinbox()}を使用します。
@<code>{from_}で数値の下限、@<code>{to}で上限を設定します。

プログラムを実行してみましょう。@<img>{spinbx}のように三角ボタンがついたボックスが連なるはずです。
ボタンを押して、レース番号は1~12まで、馬番は1~18までしか変更できないことを確認してみてください。

ちなみに、ボックスに直接入力する場合は、設定した上限と下限に収まらない数字や、
文字列を入力することもできてしまいます。直接入力を制限したい場合は、@<list>{denyinput}と同様に、
@<code>{state = "readonly"}を利用するとよいでしょう。ただし、この場合は馬番を空にすることができなくなります。

//image[spinbx][作成したスピンボックス][border=on]

タイムの設定にも同様にスピンボックスを使用します。

//list[spinbremain][タイム設定の追加][indent=4]{
#メニュー・ボックス・ボタンの作成
...(省略)...
kakutei = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4) #確定状況の設定

@<b>|ime_min = tk.Spinbox(root, from_ = 0, to = 9, width = 3) #勝ちタイムの設定|
@<b>|time_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3)|
@<b>|time_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)|

@<b>|ff_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3) #4Fタイムの設定|
@<b>|ff_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)|

@<b>|tf_sec = tk.Spinbox(root, from_ = 0, to = 59, width = 3) #3Fタイムの設定|
@<b>|tf_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)|
...(省略)...
#メニュー・ボックス・ボタンの配置
...(省略)...
kakutei.grid(column = 1, row = 13) #確定状況の設定

@<b>|time_min.grid(column = 1, row = 15) #勝ちタイムの設定|
@<b>|time_sec.grid(column = 1, row = 16)|
@<b>|time_sec10.grid(column = 1, row = 17)|

@<b>|ff_sec.grid(column = 1, row = 18) #4Fタイムの設定|
@<b>|ff_sec10.grid(column = 1, row = 19)|

@<b>|tf_sec.grid(column = 1, row = 20) #3Fタイムの設定|
@<b>|tf_sec10.grid(column = 1, row = 21)|
//}

=={checkbox} チェックボックス

チェックボックスとは、複数の選択肢から任意の項目を選択する際に使われるウィジェットです。
ですが、今回は簡易的なトグル(ON/OFF)スイッチとしてチェックボックスを利用してみます。

//list[checkb][チェックボックスの作成][indent=4]{
#メニュー・ボックス・ボタンの作成
...(省略)...
kakutei = ttk.Combobox(root, state="readonly", values=['　','確定','審議'], width = 4) #確定状況の設定

@<b>|record = tk.Checkbutton(root, text="レコード") #レコードの設定|

...(省略)...
#メニュー・ボックス・ボタンの配置
...(省略)...
kakutei.grid(column = 1, row = 13) #確定状況の設定

@<b>|record.grid(column = 1, row = 14) #レコードの設定|
//}

チェックボックスの作成には@<code>{Checkbutton()}を使用します。
@<code>{text}でボックスの横に表示するテキストを設定できます。

プログラムを実行して、@<img>{checkbu}のようにチェックの付け外しができるか確認しましょう。

//image[checkbu][作成したチェックボックス][border=on]

=={button} ボタン

この章の締めとして、任意の関数を実行できるボタンを作成していきます。

//list[cbutton][ボタンの作成][indent=4]{
import tkinter as tk
from tkinter import ttk
@<b>|import sys|

#掲示板を作り変える関数
@<b>|def createwindow():|
@<b>|    pass|

...(省略)...
#メニュー・ボックス・ボタンの作成
...(省略)...
tf_sec10 = tk.Spinbox(root, from_ = 0, to = 9, width = 3)

#設定内容の反映ボタン
@<b>|createbutton = tk.Button(root, text = 'create', command = createwindow)|

#プログラム終了用のボタン
@<b>|exitbutton = tk.Button(root, text = 'exit', command = sys.exit)|

...(省略)...
#メニュー・ボックス・ボタンの配置
...(省略)...
tf_sec10.grid(column = 1, row = 21)

@<b>|createbutton.grid(column = 0, row = 22) #設定内容の反映|
@<b>|exitbutton.grid(column = 1, row = 22) #プログラムの終了|
//}

ボタンの作成には@<code>{Button()}を使用します。
@<code>{text}でボタンの中のテキストを設定し、@<code>{command}でボタンが押された際に実行させる関数を設定します。

このプログラムでは、ボタンを押すと設定内容が掲示板に反映される@<code>{createbutton}、
ボタンを押すとプログラムが終了する@<code>{exitbutton}を用意しました。

@<code>{createbutton}用の関数として、新たに@<code>{createwindow}関数を定義しています。
関数の中身は次章で作成していくので、現時点では何もしない関数となっています。

プログラムの終了は、sysモジュールの@<code>{sys.exit}を使用して実装しています。

現時点での完成イメージを@<img>{complete}に示します。createボタンを押下できること、
exitボタンを押すとプログラムが終了することを確認してください。

これでこの章は終わりです！

//image[complete][この章の完成イメージ][border=on]