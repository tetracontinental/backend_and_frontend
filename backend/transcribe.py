from faster_whisper import WhisperModel
import subprocess
import os

class Transcriber:
    def __init__(self, model_name, device="cpu", compute_type="int8"):
        self.model = WhisperModel(model_name, device=device, compute_type=compute_type)

    def download_audio(self, yt_url, file_name):
        subprocess.run(f"yt-dlp -x --audio-format mp3 -o {file_name} {yt_url}", shell=True)

    def transcribe(self, file_path):
        segments, info = self.model.transcribe(
            file_path,
            beam_size=5,
            vad_filter=True,
            without_timestamps=True
        )
        
        # 結果を整形
        transcription = {
            "language": info.language,
            "language_probability": info.language_probability,
            "segments": [{"start": segment.start, "end": segment.end, "text": segment.text} for segment in segments]
        }

        return transcription

    def cleanup(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
