import openai
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os

# Initialize the engine for text-to-speech
engine = pyttsx3.init()

# Set up your OpenAI API key
openai.api_key = 'API-KEY'

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How can I assist you today?")


def take_command():
    # Instead of using voice input, use text input
    _ = input("Enter your command: ").lower()
    return _


def open_application(query_):
    if "notepad" in query_:
        os.system("notepad.exe")
    elif "chrome" in query_:
        webbrowser.open("chrome.exe")
    elif "youtube" in query_:
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Application not available")


def openai_query(prompt):
    suyash = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return suyash.choices[0].text.strip()


if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open" in query:
            open_application(query)

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "jarvis" in query:
            response = openai_query(query)
            speak(response)

        elif "quit" in query:
            speak("Goodbye!")
            break

        # Add more commands and functions as needed

