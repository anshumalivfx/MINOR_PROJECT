import speech_recognition as sr
import pyttsx3
import os
from chat import sendMessage
r = sr.Recognizer()
engine = pyttsx3.init()


def SpeakText(command):
    engine = pyttsx3.init()
    # engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')
    engine.say(command)
    engine.runAndWait()

while(1):
    MyText = input("Enter your message: ")
    MyText = MyText.lower()
    SpeakText(sendMessage(MyText))
    # try:
    #     with sr.Microphone() as source2:
    #         r.adjust_for_ambient_noise(source2, duration=0.2)
    #         audio2 = r.listen(source2)
    #         MyText = input("Enter your message: ")
    #         MyText = MyText.lower()
    #         print(sendMessage(MyText))
    #         SpeakText(sendMessage(MyText))

    # except sr.RequestError as e:
    #     print("Could not request results; {0}".format(e))
    # except sr.UnknownValueError:
    #     print("unknown error occured")