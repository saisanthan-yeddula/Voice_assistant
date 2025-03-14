import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import smtplib
import webbrowser
import openai
import requests
import os

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    try:
        voices = machine.getProperty("voices")
        machine.setProperty("voice", voices[1].id)
        machine.say(text)
        machine.runAndWait()
    except KeyboardInterrupt:
        machine.stop()
        print("Voice output interrupted.")


def listen_for_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = listener.listen(source)
            print("Recognizing...")
            command = listener.recognize_google(audio)
            print(f"User said: {command}")
            if "exit" in command.lower():
                talk("Goodbye!")
                exit(0)  # Graceful exit
            return command.lower()
    except Exception as e:
        print(f"Error: {e}")
        return ""

def get_openai_key():
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            api_key = "Entr your OpenAI API key "
            os.environ["Entr OPENAI_API_KEY"] = api_key
        openai.api_key = api_key
    except Exception as e:
        talk("Failed to get the API key.")
        print(f"Error: {e}")

def send_email(subject, body, receiver_email):
    sender_email = "enter email"
    email_password = "enter password"
    message = f"Subject: {subject}\n\n{body}"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        talk("Email sent successfully!")
    except smtplib.SMTPException:
        talk("Sorry, there was an error sending the email.")

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    talk("The current time is " + current_time)

def get_date():
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    talk("Today's date is " + current_date)

def search_wikipedia(query):
    try:
        info = wikipedia.summary(query, 1)
        talk(info)
    except wikipedia.exceptions.DisambiguationError:
        talk("There are multiple results. Please specify more.")
    except wikipedia.exceptions.PageError:
        talk("Sorry, I couldn't find any information on that topic.")

def play_song(song):
    talk("Playing " + song)
    pywhatkit.playonyt(song)

def open_website(url, name):
    talk(f"Opening {name}")
    webbrowser.open(url)

def web_search(query):
    try:
        info = wikipedia.summary(query, 1)
        talk(info)
    except wikipedia.exceptions.PageError:
        talk(f"Sorry, I couldn't find an answer. Let me search on Google.")
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")

def ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response["choices"][0]["message"]["content"]
        if reply.strip():
            talk(reply)
        else:
            talk("I'm sorry, I couldn't find an answer.")
    except Exception:
        talk("I'm sorry, I couldn't process that.")

def process_command(instruction):
    commands = {
        "play": lambda: play_song(instruction.replace("play", "").strip()),
        "time": get_time,
        "date": get_date,
        "search": lambda: search_wikipedia(instruction.replace("search", "").strip()),
        "open google": lambda: open_website("https://www.google.com", "Google"),
        "open spotify": lambda: open_website("https://www.spotify.com", "Spotify"),
        "open chat gpt": lambda: open_website("https://www.openai.com/", "ChatGPT"),
        "stop": exit_assistant,
        "exit": exit_assistant,
        "no": exit_assistant,
    }
    for cmd, func in commands.items():
        if instruction.startswith(cmd):
            func()
            return
    if "who is" in instruction or "what is" in instruction:
        web_search(instruction)
    else:
        ai_response(instruction)

def exit_assistant():
    talk("Goodbye! If you need me again, just restart the program.")
    global running
    running = False

def voice_assistant():
    get_openai_key()
    global running
    running = True
    talk("Hello! How can I assist you today?")
    try:
        while running:
            instruction = listen_for_command()
            if instruction:
                process_command(instruction)
            talk("Is there anything else I can help you with?")
    except KeyboardInterrupt:
        talk("Goodbye! Exiting the program.")
        print("\nProgram interrupted. Exiting gracefully...")


if __name__ == "__main__":
    voice_assistant()
