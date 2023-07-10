import os
import sounddevice as sd
import soundfile as sf
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    
    with open(audio_file, "rb") as audio_file:
        audio = speech.RecognitionAudio(content=audio_file.read())
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ar-AE"
    )
    
    response = client.recognize(config=config, audio=audio)
    
    if len(response.results) > 0:
        return response.results[0].alternatives[0].transcript
    else:
        return None

def save_transcription(transcription, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(transcription)

def delete_previous_data(output_file):
    if os.path.exists(output_file):
        os.remove(output_file)

def record_audio(output_file):
    duration = 10
    fs = 16000
    
    print("Recording audio...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    print("Saving audio...")
    sf.write(output_file, audio, fs)
    print("Audio saved!")

def main():
    output_file = "audio.wav"
    output_filename = "/desktop/quranID/output.txt"
    
    delete_previous_data(output_filename)
    
    record_audio(output_file)
    transcription = transcribe_audio(output_file)
    
    if transcription:
        save_transcription(transcription, output_filename)
        print("Transcription saved:", transcription)
    else:
        print("No transcription found.")

main()
