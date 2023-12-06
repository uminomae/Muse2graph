# Muse2graph

#機能：
macのダウンロードディレクトリにある.zipファイルからグラフを作成します。

#使い方：
https://github.com/uminomae/Muse2graph/blob/main/README.md
## 事前準備
1. 2つのファイルを適当な場所に保存してください。同じディレクトリにある必要があります。
	-  process_data.py
	- muse2analysis.sh
## Muse2,Mind Monitor,Dropbox
1. Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。
1. Dropboxから計測データをzipダウンロードしてください。

## ターミナルでのbashによる操作
1. ターミナル上で、muse2analysis.shを保存したディレクトリに移動してください  
例
```bash 
	cd /Users/username/Documents
```
1. muse2analysis.shを実行してください。グラフが作成されます。  
例　
```bash
	sh ./muse2analysis.sh 1 title
```
- `sh ./muse2analysis.sh`は実行するbash scriptの指定です。
- 最初の引数（数字1）は、.zipファイルが何番目のものかを指定します（ダウンロードフォルダ内で）。
	- 最新のファイルの場合、"1"です。
- 次の引数（文字列title）は、グラフの中央上部に表示されるタイトルです。
![mindMonitor_2023-12-03--22-22-39](https://github.com/uminomae/Muse2graph/assets/101631407/ed6034ab-c33a-484f-b6a1-78859f2832ad)
