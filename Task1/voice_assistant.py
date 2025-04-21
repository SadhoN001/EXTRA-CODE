import speech_recognition as sr     # speech recognition
import pyttsx3                      # text-to-speech
import datetime                     # To get the current time
import webbrowser                   # To open websites
import os                           # execute system commands
import psutil                       # Check running processes

engine = pyttsx3.init()             # Initialize text-to-speech engine

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio
    try:
        command = recognizer.recognize_google(audio).lower() # Convert audio to text
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return ""

# def is_process_running(process_name):
#     """Check if a process is running."""
#     for process in psutil.process_iter(['pid', 'name']):
#         if process_name.lower() in process.info['name'].lower():
#             return True
#     return False

def execute_command(command):
    """Perform actions based on voice commands."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
        
    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        speak("Opening github.")
        
    elif "close github" in command:
        # if is_process_running("chrome.exe"):  # Check if Chrome is open
            os.system("taskkill /IM chrome.exe /F") 
            speak("Closing GitHub.")
        # else:
        #     speak("GitHub was already closed.")
    
    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Sadhon kumar dev . Thank you!")
        exit()

    else:
        speak("Sorry, I can't perform that task yet.")

# Main loop
if __name__ == "__main__":
    speak("Hello Sadhon! I am your voice assistant. How can I help you?")
    while True:
        command = recognize_speech()
        if command:
            execute_command(command)
