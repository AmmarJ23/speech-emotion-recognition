import pyaudio
import speech_recognition as sr
from emotions import create_feature, vectorizer, clf, emoji_dict

def processAudio(userChoice, audio):

    #user chooses english
    if(userChoice == 0):
        #recognise english
        try:
            transcribedTextEN = r.recognize_google(audio, language="en-GB")
            print("Google Speech Recognition - English: " + transcribedTextEN)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print(transcribedTextEN)
        return transcribedTextEN
        
    #user chooses chinese
    if(userChoice == 1):
         #recognise chinese
        try:
            transcribedTextCH = r.recognize_google(audio, language="zh")
            print("Google Speech Recognition - Chinese: " + transcribedTextCH)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return transcribedTextCH

    #user chooses malay
    if(userChoice == 2):
        #recognise malay
        try:
            transcribedTextMY = r.recognize_google(audio, language="ms-My")
            print("Google Speech Recognition - Malay: " + transcribedTextMY)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return transcribedTextMY

mainTextEN = mainTextCH = mainTextMY = mainText = ""
userChoice = 0

while(True):

    print("[0]=English\n[1]=Chinese\n[2]=Malay")
    input(userChoice)

    #listen for speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recording...")
        audio = r.listen(source)

    mainTextTemp = processAudio(userChoice, audio)
    mainText = mainText + "." + mainTextTemp
    
    with open("Transcribed_Text\Transcribed Text.txt", 'w') as f:
        f.write(mainText)
        f.close
    
    features = create_feature(mainText)
    features = vectorizer.transform(features)
    prediction = clf.predict(features)[0]
    print(mainText, emoji_dict[prediction])
    print("\n")