"""A beginner-friendly, speech-controlled desktop assistant."""

from datetime import datetime
import re
import threading
import urllib.parse
import webbrowser

import pyttsx3
import speech_recognition as sr


def create_speech_engine():
    """Create the text-to-speech engine once and reuse it."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    return engine


def speak(engine, message):
    """Print a response and read it aloud."""
    print(f"Assistant: {message}")
    engine.say(message)
    engine.runAndWait()


def listen(recognizer, engine):
    """Record one phrase and turn it into lowercase text."""
    try:
        with sr.Microphone() as microphone:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
            audio = recognizer.listen(microphone, timeout=5, phrase_time_limit=8)

        # This recognizer uses Google's web speech service, so internet is needed.
        words = recognizer.recognize_google(audio)
        print(f"You: {words}")
        return words.lower().strip()
    except sr.WaitTimeoutError:
        speak(engine, "I did not hear anything. Please try again.")
    except sr.UnknownValueError:
        speak(engine, "Sorry, I did not understand. Please repeat that.")
    except sr.RequestError:
        speak(engine, "Speech recognition is unavailable. Check your internet connection.")
    except OSError:
        speak(engine, "I cannot access a microphone. Check that one is connected and enabled.")

    return ""


def search_topic(command):
    """Return the words to search for, or an empty string if this is not a search."""
    prefixes = (
        "search for ",
        "search ",
        "google ",
        "look up ",
        "tell me about ",
        "what is ",
        "who is ",
    )
    for prefix in prefixes:
        if command.startswith(prefix):
            return command[len(prefix):].strip()
    return ""


def set_reminder(command, engine):
    """Schedule a reminder phrased as 'remind me in 2 minutes to stretch'."""
    match = re.search(
        r"remind me in (\d+) (second|seconds|minute|minutes) to (.+)", command
    )
    if not match:
        speak(engine, "Try saying: remind me in 2 minutes to stretch.")
        return

    amount = int(match.group(1))
    unit = match.group(2)
    message = match.group(3).strip()
    seconds = amount * 60 if unit.startswith("minute") else amount

    speak(engine, f"Okay, I will remind you in {amount} {unit} to {message}.")

    # Use a separate speech engine in the timer callback because it runs in a background thread.
    def announce_reminder():
        reminder_engine = create_speech_engine()
        speak(reminder_engine, f"Reminder: {message}")

    timer = threading.Timer(seconds, announce_reminder)
    timer.daemon = True
    timer.start()


def handle_command(command, engine):
    """Perform one beginner command. Return False when the user wants to quit."""
    if not command:
        return True

    if "hello" in command or "hi assistant" in command:
        speak(engine, "Hello! How can I help you?")
    elif "can you hear me" in command or "why don't you hear" in command:
        speak(engine, "Yes, I can hear you. I understood: " + command)
    elif "time" in command and "date" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(engine, f"It is {current_time} on {current_date}.")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(engine, f"The time is {current_time}.")
    elif "date" in command or "day is it" in command:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(engine, f"Today is {current_date}.")
    elif "remind me" in command:
        set_reminder(command, engine)
    elif command in {"quit", "exit", "stop", "goodbye"}:
        speak(engine, "Goodbye!")
        return False
    else:
        topic = search_topic(command)
        if topic:
            search_url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(topic)
            speak(engine, f"Searching the web for {topic}.")
            webbrowser.open(search_url)
        else:
            speak(engine, "I do not know that command yet. Please try again.")

    return True


def main():
    engine = create_speech_engine()
    recognizer = sr.Recognizer()
    speak(engine, "Voice assistant is ready. Say hello, ask for the time or date, or ask me to search for something.")

    keep_running = True
    try:
        while keep_running:
            command = listen(recognizer, engine)
            keep_running = handle_command(command, engine)
    except KeyboardInterrupt:
        speak(engine, "Assistant stopped. Goodbye!")


if __name__ == "__main__":
    main()
