# Muse2graph

機能：
macのダウンロードディレクトリにある.zipファイルからグラフを作成します。

使い方：
Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。
Dropboxから計測データをzipダウンロードしてください。

ファイルを適当な場所に保存してください
ターミナルで保存したディレクトリに移動してmuse2analysis.shを実行してください（ex. cd /Users/username/Documents）
例
```
sh ./muse2analysis.sh 1 title
```
.shに渡す最初の引数（数字）は、ダウンロードフォルダ内の.zipファイルが何番目のものかを指定します。最新の.zipの場合、"1"
次の引数（文字列）は、グラフの中央上部に表示されるタイトルです。
