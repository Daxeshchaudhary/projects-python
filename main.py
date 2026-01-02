import speech_recognition as sr
import webbrowser
import pyttsx3
import music


Recognizer=sr.Recognizer()
ttsx=pyttsx3.init()
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkdein" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    
    
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print(" error; {0}".format(e))