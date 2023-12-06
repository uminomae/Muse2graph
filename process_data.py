#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import sys
import os
from datetime import datetime
# コマンドライン引数の数を確認
if len(sys.argv) < 2:
    print("Error: 数字が指定されていません。")
    sys.exit(1)

# 日本語フォントの設定
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# コマンドライン引数からCSVファイルのパスを取得
csv_file_path = sys.argv[1]
csv_file_name = os.path.splitext(os.path.basename(csv_file_path))[0]
# オプショナルなグラフタイトル（引数が与えられていれば使用、そうでなければデフォルトタイトルを使用）
graph_title = sys.argv[2] if len(sys.argv) > 2 else 'Average Brainwave Patterns Over Time (Resampled at 10-second Intervals)'

# 保存するディレクトリのパス（例: 'saved_plots'）
save_directory = 'saved_plots'
# ディレクトリが存在しない場合は作成
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# PNGファイルの名前をCSVファイル名と同じにし、保存ディレクトリに配置
png_file_name = f"{save_directory}/{csv_file_name}.png"
# CSVファイルの読み込み
data = pd.read_csv(csv_file_path)


# -----------------------
# ここにデータ処理とグラフ生成のコードを挿入
# -----------------------
# TimeStamp列をdatetime型に変換
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])

# データの最後のタイムスタンプから60分前の時刻を計算
end_time = data['TimeStamp'].max()
start_time_60min = end_time - pd.Timedelta(minutes=60)
# 直近60分間のデータを抽出
recent_60min_data = data[data['TimeStamp'] >= start_time_60min]

# TimeStamp列をインデックスに設定
recent_60min_data.set_index('TimeStamp', inplace=True)

# 必要な列が存在するか確認
required_columns = ['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10', 'Theta_TP9']
missing_columns = [col for col in required_columns if col not in recent_60min_data.columns]
if missing_columns:
    print(f"Missing columns: {missing_columns}")
    sys.exit(1)

# 数値型の列のみを選択
recent_60min_numeric = recent_60min_data.select_dtypes(include=['float64', 'int64'])

# 各波形の平均値を計算
recent_60min_numeric['Average_Delta'] = recent_60min_numeric[['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10']].mean(axis=1)
recent_60min_numeric['Average_Delta']  = recent_60min_numeric[['Delta_TP9', 'Delta_AF7', 'Delta_AF8', 'Delta_TP10']].mean(axis=1)
recent_60min_numeric['Average_Theta']  = recent_60min_numeric[['Theta_TP9', 'Theta_AF7', 'Theta_AF8', 'Theta_TP10']].mean(axis=1)
recent_60min_numeric['Average_Alpha']  = recent_60min_numeric[['Alpha_TP9', 'Alpha_AF7', 'Alpha_AF8', 'Alpha_TP10']].mean(axis=1)
recent_60min_numeric['Average_Beta']  = recent_60min_numeric[['Beta_TP9', 'Beta_AF7', 'Beta_AF8', 'Beta_TP10']].mean(axis=1)
recent_60min_numeric['Average_Gamma']  = recent_60min_numeric[['Gamma_TP9', 'Gamma_AF7', 'Gamma_AF8', 'Gamma_TP10']].mean(axis=1)

# リサンプリング
resampled_recent_data = recent_60min_numeric.resample('10S').mean()

# データフレームの各行を反復処理し、有効なデータがある最初の行を見つける
valid_start_time = None
for timestamp, row in resampled_recent_data.iterrows():
    if not row.isna().all():  # 行に少なくとも1つの有効なデータがある場合
        valid_start_time = timestamp
        break

# 有効な開始日時が見つかった場合
# if valid_start_time is not None:
    # x軸の値を開始時刻からの経過時間に設定
resampled_recent_data['Elapsed_Minutes'] = (resampled_recent_data.index - valid_start_time).total_seconds() / 60
# else:
#     print("有効な開始日時が見つかりませんでした。")

# 各波形の移動平均を計算
window_size = 6
for col in ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma']:
    col_name = f'Rolling_Avg_{col}'
    resampled_recent_data[col_name] = resampled_recent_data[f'Average_{col}'].rolling(window=window_size).mean()

# グラフのプロット
plt.figure(figsize=(15, 8))
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Average_Delta'], label='Average Delta', color='red', linewidth=1, alpha=0.5)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Average_Theta'], label='Average Theta', color='purple', linewidth=1, alpha=0.5)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Average_Alpha'], label='Average Alpha', color='blue', linewidth=1, alpha=0.5)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Average_Beta'], label='Average Beta', color='green', linewidth=1, alpha=0.5)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Average_Gamma'], label='Average Gamma', color='yellow', linewidth=1, alpha=0.5)

# 移動平均のプロット（破線で表示）
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Rolling_Avg_Delta'], label='Rolling Avg Delta', color='darkred', linewidth=2)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Rolling_Avg_Theta'], label='Rolling Avg Theta', color='indigo', linewidth=2)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Rolling_Avg_Alpha'], label='Rolling Avg Alpha', color='darkblue', linewidth=2)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Rolling_Avg_Beta'], label='Rolling Avg Beta', color='darkgreen', linewidth=2)
plt.plot(resampled_recent_data['Elapsed_Minutes'], resampled_recent_data['Rolling_Avg_Gamma'], label='Rolling Avg Gamma', color='olive', linewidth=2)


time_difference = end_time - valid_start_time

# 時間差を分単位で表示（四捨五入）
total_minutes = round(time_difference.total_seconds() / 60)

# グラフに開始日時、終了日時、および時間差を表示
plt.text(x=0.01, y=0.01, 
        s=f"開始日時: {valid_start_time.strftime('%Y-%m-%d %H:%M:%S')}\n終了日時: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n合計時間: {total_minutes}分",
        transform=plt.gca().transAxes, fontsize=9, verticalalignment='bottom')
# 有効な開始日時が見つかった場合、グラフに表示
# if valid_start_time is not None:
    # 開始日時と終了日時の差を計算
    # time_difference = end_time - valid_start_time

    # # 時間差を分単位で表示（四捨五入）
    # total_minutes = round(time_difference.total_seconds() / 60)

    # # グラフに開始日時、終了日時、および時間差を表示
    # plt.text(x=0.01, y=0.01, 
    #         s=f"開始日時: {valid_start_time.strftime('%Y-%m-%d %H:%M:%S')}\n終了日時: {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n合計時間: {total_minutes}分",
    #         transform=plt.gca().transAxes, fontsize=9, verticalalignment='bottom')

# else:
#     print("有効な開始日時が見つかりませんでした。")

# グラフの設定
plt.title(graph_title)
plt.xlabel('Time')
plt.ylabel('Average Amplitude')
plt.xticks(rotation=45)
plt.tight_layout()
# y軸の上限値と下限値を設定
plt.ylim(-0.6, 1.8)
# 判例を右下に固定
plt.legend(loc='lower right')

# 移動平均の説明文
plt.text(x=0.01, y=0.95, 
         s="10秒ごとの平均値とその移動平均 (直前の5点のデータとその点自身、合計6点の平均値)\n"
            "10-second averages and their moving averages (Window size: 6)\n",
         transform=plt.gca().transAxes, fontsize=9, verticalalignment='top', horizontalalignment='left',
         bbox=dict(facecolor='white', alpha=0.5))

# ---------------
# グラフの保存（オプション）
plt.savefig(png_file_name)
import subprocess
# ファイルが存在する場合に開く
if os.path.exists(png_file_name):
    # MacOSの場合
    subprocess.run(['open', png_file_name])
