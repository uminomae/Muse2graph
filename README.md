# Muse2graph

# 機能：
- macのダウンロードディレクトリにある.zipファイルからグラフを作成します。
- 直近60分間のデータからグラフを作成します。※60分未満の場合でも出力できます。
- 移動平均線は直近5つのデータポイントとの平均です。
<img width="900" alt="mindMonitor_2023-12-03--22-22-3" src="https://github.com/uminomae/Muse2graph/assets/101631407/ed6034ab-c33a-484f-b6a1-78859f2832ad">

# 使い方：
## 事前準備
1. 2つのファイルを適当な場所に保存してください。同じディレクトリにある必要があります。
	- process_data.py
	- muse2analysis.sh  
※saved_plots,extracted_dataディレクトリは自動で作成されます。
<img width="150" alt="スクリーンショット 2023-12-06 9 20 18" src="https://github.com/uminomae/Muse2graph/assets/101631407/08d155ab-2fee-4679-9435-9caae34e6dc7">  

## Muse2,Mind Monitor,Dropbox
1. Muse2使用時に、Mind Monitorアプリを使用してDropboxに転送（標準機能）してください。
<img width="200" alt="スクリーンショット 2023-12-06 10 29 47" src="https://github.com/uminomae/Muse2graph/assets/101631407/63cd19f5-c4ba-4cff-8430-10354c2c3462">

1. Dropboxから計測データ(zip)をダウンロードディレクトリにダウンロードしてください。  
<img width="300" alt="スクリーンショット 2023-12-06 9 10 12" src="https://github.com/uminomae/Muse2graph/assets/101631407/dd0114c0-6a35-40c6-9cfb-84a5210bb1aa">  

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
<img width="516" alt="スクリーンショット 2023-12-06 9 23 53" src="https://github.com/uminomae/Muse2graph/assets/101631407/5d33be41-71d0-451b-80e9-9f483fe326a3">

- `sh ./muse2analysis.sh`は実行するbash scriptの指定です。
- 最初の引数（数字1）は、.zipファイルが何番目のものかを指定します（ダウンロードフォルダ内で）。
	- 最新のファイルの場合、"1"です。
- 次の引数（文字列title）は、グラフの中央上部に表示されるタイトルです。
例  下記のような出力の後、カレントディレクトリのsaved_plotsディレクトリにグラフが保存され、同時にディスプレイに画像が表示されます。  

<img width="2091" alt="スクリーンショット 2023-12-06 9 27 32" src="https://github.com/uminomae/Muse2graph/assets/101631407/915766f5-104f-4718-ade2-fbfb0bffd4a4">

参考:【Muse2（BMI）で脳波を測ってみた！ | TECH | NRI Digital】 https://www.nri-digital.jp/tech/20211228-7840/  
参考:【Mind Monitor】 https://mind-monitor.com/Chart.php
