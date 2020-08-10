import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening to Microphone...")
    audio_data = rec.record(source=source,duration=3)
    text = rec.recognize_google(audio_data)
    print(text)
