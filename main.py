print('Lets make a project using python:')
import speech_recognition as sr
import webbrowser
import webbrowser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe %s"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
import pyttsx3
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('volume',1.0)  # max volume
engine.setProperty('rate',170)    # Speed control


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

apps ={
    "google": ("(https://google.com)", "Google"),
    "youtube": ("(https://youtube.com)", "YouTube"),   
    "instagram": ("(https://instagram.com)", "Instagram"),
    "linkedin": ("(https://linkedin.com)", "LinkedIn"),
    "chatgpt": ("(https://chatgpt.com)", "ChatGPT"),
    "github": ("(https://github.com)", "GitHub")

}

def processCommand(command):
    command = command.lower()

    for app in apps:
        if f"open {app}" in command:
            speak(f"Sure sir,Opening {apps[app][1]}")
            time.sleep(2.5)
            webbrowser.get('chrome').open(apps[app][0])
            return
    
    speak("Sorry I did'nt understand the command:")

    engine.setProperty('volume',1.0)  # max volume
    engine.setProperty('rate',170)    # Speed control



if __name__ == "__main__":
    speak("Hello sir, how can i help you")
    
    while True:
        r = sr.Recognizer()
        print("Recognizing")

        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                if "jarvis" in word.lower():
                    speak("Yes sir")

                    # the below code for listening 
                    with sr.Microphone() as source:
                        print("Jarvis Active")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)
        except Exception as e:
            print("Error", e)
                
                


    