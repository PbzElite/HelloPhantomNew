import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
    
try:
    print(r.recognize_vosk(audio, show_All=True))
except sr.UnknownValueError:
    print("what are you doing")