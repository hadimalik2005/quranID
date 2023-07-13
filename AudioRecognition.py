import sounddevice as sd
import soundfile as sf
from google.cloud import speech_v1p1beta1 as speech
import os

def recordAudio(filename, duration, sampleRate):
    print("Recording audio...")
    audio = sd.rec(int(duration * sampleRate), channels=1, blocking=True)
    sd.wait()
    print("Recording complete")
    sf.write(filename, audio, sampleRate)

def transcribeAudio(filename):
    client = speech.SpeechClient().from_service_account_file('key.json')

    with open(filename, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="ar-SA",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcript = result.alternatives[0].transcript[::-1]
        transcripts.append(transcript)

    return transcripts

def main():
    filename = "recordedAudio.wav"
    duration = 10
    sampleRate = 44100

    recordAudio(filename, duration, sampleRate)
    transcripts = transcribeAudio(filename)
    
    for transcript in transcripts:
        print(transcript)

    os.remove(filename)

if __name__ == "__main__":
    main()
