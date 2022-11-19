import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyjokes 
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        recognizer.adjust_for_ambient_noise(source)
        audio =recognizer.listen(source)
        try:
            print("recognizing........")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            sptext()
        
#sptext( )

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate= engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':

    
    
        while True:
            data1 =sptext().lower()
            if "your name" in data1:
                name = 'my name is something'
                speechtx(name)
            elif 'old are you' in data1:
                    age =' i am one year old'
                    speechtx(age)
            elif 'time' in data1:
                    time = datetime.datetime.now().strftime('%I%M%p')
                    speechtx(time)
            elif 'youtube' in data1:
                    webbrowser.open('https://www.youtube.com/')
            elif 'joke' in data1:
                    joke_1=pyjokes.get_joke(language='en',category='neutral')
                    speechtx(joke_1)
            elif  'exit' in data1 or 'close' in data1:
                speechtx('THank u')
                print( 'thank u')
                break
            time.sleep(5)


