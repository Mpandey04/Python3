import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
ttsx=pyttsx3.init()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing Max")
    while True:
        
    #Listen for the wake word "Jarvis"
    #Obtain audio from the microphone
        r=sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
           
            command=r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("sphinxncould not understand audio")
        except Exception as e:
            print(" error:{0}",format(e))
    