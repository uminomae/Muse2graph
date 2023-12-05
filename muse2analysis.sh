#!/bin/bash

# スクリプトのディレクトリにカレントディレクトリを変更
cd "$(dirname "$0")"

# ダウンロードディレクトリの設定
downloads_path=~/Downloads

# 引数からファイルの順番を取得
file_number=${1:-1}

# 引数からオプショナルなグラフタイトルを取得
graph_title=${2:-''}

# 指定された順番のZIPファイルを選択
zip_file=$(ls -t $downloads_path/*.zip | sed -n "${file_number}p")

# ZIPファイルの基本名を取得（拡張子を除去）
base_name=$(basename $zip_file .zip)

# ZIPファイルの解凍（解凍先を相対パスで指定）
unzip -o $zip_file -d extracted_data

# ZIPファイルと同じ基本名を持つCSVファイルを選択
csv_file=$(find extracted_data -name "${base_name}.csv" | head -n 1)

# Pythonスクリプトの相対パス
python_script_path="process_data.py"

# Pythonスクリプトの実行（CSVファイルのパスとグラフタイトルを引数として渡す）
python3 $python_script_path $csv_file "$graph_title"

