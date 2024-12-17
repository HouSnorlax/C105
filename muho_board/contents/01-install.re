= インストール

//abstract{
Pythonの環境構築を行います。
//}

#@#//makechaptitlepage[toc=on]



== Pythonのインストール

//note{
すでにPythonの環境がある方は@<chapref>{02-tuto}に進んでください。
//}

はじめに、Pythonの公式サイト(@<href>{https://www.python.org/})にアクセスしてください。

公式サイトの上部のメニューに@<B>{Downloads}という項目があるので、
そこにカーソルを合わせると@<img>{download}のようにDownload for Windowsというメニューが表示されます。
メニューの@<B>{Python 3.13.1}と書かれたボタンを押して、インストーラーをダウンロードしてください。

//image[download][pythonのダウンロード][border=on]

インストーラーを起動すると、@<img>{path}のようなウィンドウが表示されます。
ここで、下部の@<B>{Add python.exe to PATHに必ずチェックを入れてください}。
チェックを入れないと、Pythonを実行することができません。
(ものすごく面倒な設定をすることになります)

チェックを入れたら、Install Nowを押してPythonをインストールします。

//image[path][インストーラー][border=on]

インストールが完了すると、様々なリンクやボタンが表示されたウィンドウが出ますが、
それらは全て無視してCloseボタンを押してください。

=={pythontest} Pythonの動作確認

Windowsの検索ボックスに@<code>{cmd}と入力して、コマンドプロンプトを起動します。

コマンドプロンプトを起動したら、@<list>{wakeuppython}のように入力し、pythonを実行します。

//terminal[wakeuppython][pythonの実行]{
$ C:\Users\username> @<userinput>{python} 
//}

実行すると@<img>{pythontest}のように、対話モードと呼ばれるものが起動します。
試しに@<code>{print('Hello World!')}を実行して、動作を確認しましょう、

//image[pythontest][Pythonの対話モード][border=on]

これでインストールは終わりです。