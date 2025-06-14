import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize text-to-speech
engine = pyttsx3.init()

# Make voice assistant talk
def speak(text):

    engine.say(text)
    engine.runAndWait()

# Captures and converts voice to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = recognizer.listen(source)
        try:
             command = recognizer.recognize_google(voice)
             print(f"You: {command}")
             return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I can't connect to the service.")
            return ""

def run_assistant():
    speak("Hi! I'm your assistant.")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I help?")
        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p') # Timme in 12 hour format
            speak(f"The time is {time}")
        elif "date" in command:
            date = datetime.date.today().strftime('%B %d, %Y')
            speak(f"Today's date is {date}")
        elif "search" in command:
            topic = command.replace("search", "").strip()
            speak(f"Searching {topic}")
            pywhatkit.search(topic) #Open web browser and search the topic in Google
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't do that yet.")

run_assistant()