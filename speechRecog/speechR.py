import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    audio1 = r.record(source)
    r.recognize_google(audio1)
    # audio2 = r.record(source, duration= 4)


# jackhammer = sr.AudioFile('jackhammer.wav')

# with jackhammer as source:
#     r.adjust_for_ambient_noise(source)
#     audio3 = r.record(source)
   

# r.recognize_google(audio2)
# r.recognize_google(audio3)
