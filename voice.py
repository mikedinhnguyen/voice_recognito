import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=12000) as source:
        r.energy_threshold = 100
        print("start speaking!")
        audio = r.record(source, duration=5)
        transcript = ""
        try:
            transcript = r.recognize_google(audio, language="en-US")
            print(transcript)
            # speak(transcript)
        except sr.UnknownValueError:  # error: recognizer does not understand
            speak("I did'nt get that")
            exit()
        except Exception as e:
            print("Exception: " + e)
    return transcript

text = get_audio()
if "hello" in text:
    speak("hello, how are you?")