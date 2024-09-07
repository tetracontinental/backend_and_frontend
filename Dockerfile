# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.9-slim

#要求されるffmpegをインストール
RUN apt install -y ffmpeg

# 作業ディレクトリを作成
WORKDIR /app

# ローカルの依存ファイルをコンテナにコピー
COPY requirements.txt requirements.txt

# 依存パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .

# アプリケーションを実行
CMD ["python", "transcribe.py"]
