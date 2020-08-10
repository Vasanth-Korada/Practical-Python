from gtts import gTTS
from playsound import playsound

myText = "Hello Everyone, Welcome to infy tech"

obj = gTTS(text=myText,lang='en',slow=False)

obj.save("welcome.mp3")

try:
    playsound("welcome.mp3")
    print("Completed Successfully")
except:
    print("Error")




