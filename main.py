import pyaudio
import PySimpleGUI as sg
import speech_recognition as sr

mainText = " "

while(True):

    #listen for speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        audio = r.listen(source)

    #transcribe speech into string
    try:
        transcribedText = r.recognize_google(audio)
        print("Google Speech Recognition successful: " + transcribedText)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #add transcribed text into main text file
    mainTextTemp = str(transcribedText)
    mainText = mainText + " " + mainTextTemp

    with open("Transcribed Text.txt", 'w') as f:
        f.write(mainText)
        f.close