FROM python:3.9-slim

WORKDIR /app
COPY app.py /app

RUN pip install streamlit requests

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
