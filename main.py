import pyaudio
import PySimpleGUI as sg
import speech_recognition as sr

mainTextEN = mainTextCH = mainTextMY = " "

while(True):

    #listen for speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        audio = r.listen(source)

    #recognise english
    try:
        transcribedTextEN = r.recognize_google(audio, language="en-GB")
        print("Google Speech Recognition - English: " + transcribedTextEN)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #recognise chinese
    try:
        transcribedTextCH = r.recognize_google(audio, language="zh")
        print("Google Speech Recognition - Chinese: " + transcribedTextCH)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #recognise malay
    try:
        transcribedTextMY = r.recognize_google(audio, language="ms-My")
        print("Google Speech Recognition - Malay: " + transcribedTextMY)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #recognise japanese
    try:
        transcribedTextJP = r.recognize_google(audio, language="ja-JP")
        print("Google Speech Recognition - Malay: " + transcribedTextJP)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #english transcribed text into main file
    mainTextTempEN = str(transcribedTextEN)
    mainTextEN = mainTextEN + ". " + mainTextTempEN

    #chinese transcribed text into main file
    mainTextTempCH = str(transcribedTextCH)
    mainTextCH = mainTextCH + ". " + mainTextTempCH

    #malay transcribed text into main file
    mainTextTempMY = str(transcribedTextMY)
    mainTextMY = mainTextMY + ". " + mainTextTempMY

    with open("Transcribed Text - EN.txt", 'w') as f:
        f.write(mainTextEN)
        f.close
    
    #with open("Transcribed Text - CH.txt", 'w') as f:
    #    f.write(mainTextCH)
    #    f.close

    with open("Transcribed Text - MY.txt", 'w') as f:
        f.write(mainTextMY)
        f.close