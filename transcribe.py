# `faster_whisper`ライブラリからWhisperModelクラスをインポート
from faster_whisper import WhisperModel

# サブプロセスを扱うための`subprocess`モジュールをインポート
import subprocess

# 処理対象のYouTube動画のIDを指定
YOUTUBE_ID = "KFKCeVxGdRk"  # Youtube ID

# ダウンロードする音声ファイルの名前をYouTube IDを使って設定
AUDIO_FILE_NAME = f"{YOUTUBE_ID}.mp3"

# 出力ファイルの名前を設定
OUTPUT_FILE_NAME = "output.txt"

# YouTubeから音声をダウンロードする関数を定義
def dl_yt(yt_url):
    # `yt-dlp`コマンドを使用して、指定したYouTubeのURLから音声をMP3形式でダウンロード
    subprocess.run(f"yt-dlp -x --audio-format mp3 -o {AUDIO_FILE_NAME} {yt_url}", shell=True)

# YouTubeのURLを作成し、音声のダウンロードを実行
dl_yt(f"https://youtu.be/{YOUTUBE_ID}")

# Whisperモデルのインスタンスを作成（"large-v3"モデルを使用し、CPU上で計算を行い、INT8型で計算）
model = WhisperModel("large-v3", device="cpu", compute_type="int8")

# ダウンロードした音声ファイルをテキストに変換
segments, info = model.transcribe(
    AUDIO_FILE_NAME,       # 音声ファイルの名前
    beam_size=5,           # ビームサーチのサイズ（解の探索の幅）       # 音声活動検出フィルタを使用
    without_timestamps=True, # タイムスタンプなしでテキストを出力
)

# 出力ファイルを開いて、結果を書き込む
with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
    # 検出された言語とその確率を書き込む
    file.write(f"Detected language '{info.language}' with probability {info.language_probability:.6f}\n\n")

    # 各音声セグメントを開始時間、終了時間、テキストと共に書き込む
    for segment in segments:
        file.write(f"{segment.text}\n")
# ダウンロードした音声ファイルを削除
import os
os.remove(AUDIO_FILE_NAME)
