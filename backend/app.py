from flask import Flask, request, jsonify
from transcribe import Transcriber

app = Flask(__name__)

# Whisperモデルの設定
model_name = "large-v3"
transcriber = Transcriber(model_name)

@app.route('/process', methods=['POST'])
def process_file():
    yt_url = request.form.get('yt_url')
    if not yt_url:
        return jsonify({"error": "YouTube URL is required"}), 400

    file_name = "temp_audio.mp3"

    # 音声ファイルをダウンロードして文字起こし
    transcriber.download_audio(yt_url, file_name)
    transcription = transcriber.transcribe(file_name)
    transcriber.cleanup(file_name)

    return jsonify(transcription)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
