import streamlit as st
import requests

st.title('YouTube Audio Transcriber')

yt_url = st.text_input("Enter YouTube URL")

if st.button('Transcribe'):
    if yt_url:
        response = requests.post('http://localhost:5000/process', data={'yt_url': yt_url})

        if response.status_code == 200:
            result = response.json()
            st.write("Detected language:", result.get("language"))
            st.write("Language probability:", result.get("language_probability"))
            st.write("Transcription:")
            for segment in result.get("segments", []):
                st.write(f"[{segment['start']:.2f}s -> {segment['end']:.2f}s] {segment['text']}")
        else:
            st.write("Failed to process the request. Please try again.")
    else:
        st.write("Please enter a YouTube URL.")
