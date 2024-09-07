FROM python:3.9-slim

WORKDIR /app
COPY app.py /app

RUN pip install Flask yt-dlp faster_whisper

CMD ["python", "app.py"]
