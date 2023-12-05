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






# # スクリプトのディレクトリにカレントディレクトリを変更
# cd "$(dirname "$0")"


# # ダウンロードディレクトリの設定
# downloads_path=~/Downloads

# # 引数からファイル名を取得
# file_name=$1

# # 引数からファイルの順番を取得（デフォルトは1）
# file_number=${2:-1}

# # 指定されたファイル名と一致し、指定された順番のZIPファイルを選択
# zip_file=$(ls -t $downloads_path/$file_name*.zip | head -n $file_number | tail -n 1)

# # ZIPファイルの解凍（解凍先を相対パスで指定）
# unzip -o $zip_file -d extracted_data

# # 同じ名前を持つCSVファイルを探す
# csv_file=$(find extracted_data -name "${file_name}*.csv" | head -n 1)

# # Pythonスクリプトの相対パス
# python_script_path="process_data.py"

# # Pythonスクリプトの実行（CSVファイルのパスを引数として渡す）
# python3 $python_script_path $csv_file


# # Pythonスクリプトの実行（グラフタイトルを引数として渡す）
# python3 $python_script_path $csv_file "${@:3}"

# ----
# #!/bin/bash

# # スクリプトのディレクトリにカレントディレクトリを変更
# cd "$(dirname "$0")"

# # ダウンロードディレクトリの設定
# downloads_path=~/Downloads

# # # 引数が与えられた場合、その数値を使用。そうでなければ1（最新のファイル）
# # file_number=${1:-1}

# # 引数からファイル名を取得
# file_name=$1

# # ZIPファイルのリストを作成し、指定された番号のファイルを選択
# latest_zip=$(ls -t $downloads_path/*.zip | head -n $file_number | tail -n 1)

# # ZIPファイルの名前から拡張子を除いた基本名を取得
# base_name=$(basename "$latest_zip" .zip)

# # ZIPファイルの解凍（解凍先を相対パスで指定）
# unzip -o $latest_zip -d extracted_data

# # 同じ基本名を持つCSVファイルを探す
# csv_file=$(find extracted_data -name "${base_name}.csv")

# # Pythonスクリプトの相対パス
# python_script_path="process_data.py"

# # Pythonスクリプトの実行
# python3 $python_script_path $csv_file