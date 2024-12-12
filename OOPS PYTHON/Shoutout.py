import pyttsx3
engine = pyttsx3.init()
names=["Shikher","jain","Sonu","This is me "]
# names=["Paagaal","hai","kya","puri"]
for name in names:
    engine.say(f" {name}")
    engine.runAndWait()