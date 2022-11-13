import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from playsound import playsound


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query


s = takeCommand()
print(s)

text_val = s

language = 'en'
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("exam.mp3")
playsound("exam.mp3")
