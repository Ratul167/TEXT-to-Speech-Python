
from ast import While
import pyttsx3
import speech_recognition


while True:
 engine =pyttsx3.init()




 answer =input("What do yo want to convert to speech :")

 engine.say(answer)





 engine.runAndWait()

 again=input("Do you want to do it again ?:")
 if again !="yes":
   break

 print(answer)
print("Bye bye")

