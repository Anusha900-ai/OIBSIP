# Beginner Python Voice Assistant

This starter project listens to one spoken phrase at a time and can greet you, tell the date or time, and search the web. It uses Python's built-in `datetime`, `urllib.parse`, and `webbrowser` modules, plus `SpeechRecognition` and `pyttsx3`.

## Step-by-step setup (Windows)

1. **Install Python 3.9 or newer.** During installation, enable the option to add Python to PATH. Open PowerShell and check with `python --version`.
2. **Open this folder in your editor** and open a terminal in the folder containing `voice_assistant.py`.
3. **Create a virtual environment.** This keeps this project's packages separate:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, or install packages with `.venv\Scripts\python.exe -m pip install -r requirements.txt`.

4. **Install the libraries:**

   ```powershell
   python -m pip install -r requirements.txt
   ```

   The `audio` extra installs PyAudio, which lets SpeechRecognition access your microphone. If this step fails, see the [SpeechRecognition installation notes](https://pypi.org/project/SpeechRecognition/).

5. **Allow microphone access** for your terminal/editor in Windows privacy settings. Connect headphones if speaker audio is feeding back into the microphone.
6. **Run the assistant:**

   ```powershell
   python voice_assistant.py
   ```

7. **Try these phrases:** “Hello”, “What time is it?”, “What is the date?”, “Search for beginner Python projects”, and “Stop”. The browser opens for search commands; say “stop” to exit.

## How the program works

1. `main()` creates a speech recognizer and a text-to-speech engine, then repeats until you say “stop”.
2. `listen()` opens the microphone, records a short phrase, and asks the speech recognition service to convert audio into text.
3. The result is lowercased so the program can compare it without worrying about capital letters.
4. `handle_command()` checks the text with `if` / `elif` conditions. It uses `datetime.now()` for time and date, and `webbrowser.open()` to open a URL for a search.
5. `speak()` both prints and speaks every assistant response. The exception handlers give a spoken retry message when speech is unclear, the service is unavailable, or a microphone cannot be accessed.

## Beginner concepts to notice

- **Imports** make existing tools available to your program.
- **Functions** (`listen`, `speak`, `handle_command`) give each job a name and keep the code organized.
- **Variables** such as `command` and `current_time` hold values while the program runs.
- **Conditions** choose an action based on what was heard.
- **A loop** lets the assistant handle more than one command.
- **`try` / `except`** handle expected failures without crashing immediately.

## Privacy and network behavior

The program captures microphone audio only while `listen()` is running. `recognize_google()` sends that audio to Google's speech recognition service for transcription; an internet connection is required, and Google's service terms/privacy policy apply. This starter does not save audio or transcripts to files. The recognized words are printed in the terminal. Search phrases are sent to Google Search when the browser opens. `pyttsx3` generates spoken replies on the computer. Avoid speaking passwords, financial details, or other sensitive information.

## Common problems

- **`No module named speech_recognition`**: activate the virtual environment and run the install command again.
- **PyAudio or microphone error**: check microphone permission and the PyAudio installation notes on PyPI; restart the terminal after changing permissions.
- **Could not understand audio**: move closer to the microphone, reduce background noise, and speak a short phrase.
- **Speech service unavailable**: check your internet connection. This starter uses online recognition.
- **No sound from `pyttsx3`**: check Windows output volume and selected output device.

## A sensible path to the advanced tier

Add one feature at a time after the beginner version works:

1. Move command phrases and responses into a JSON file for user-defined commands.
2. Add a reminder with `threading.Timer` and test it with short durations first.
3. Add weather using an API key stored in an environment variable, not in source code.
4. Add intent parsing (for example, classify varied phrases as `greeting`, `time`, or `search`) before adopting a larger NLP package.
5. Keep email for last: use a test account, environment variables for credentials, and a recipient confirmation step before sending.
6. Add general knowledge through a documented API or a small local question/answer file.

Do not commit API keys, email passwords, or other secrets to source control. For email, use a provider's current app-password/OAuth guidance; never hard-code a real mailbox password.

## Learning references

- [Beginner video: Building a Voice Assistant in Python](https://www.youtube.com/watch?v=uJaVERJfbSE)
- [SpeechRecognition on PyPI: installation and microphone setup](https://pypi.org/project/SpeechRecognition/)
- [NLP/chatbot tutorial search](https://www.youtube.com/results?search_query=Python+NLP+chatbot+intent+recognition+tutorial)
- [OpenWeatherMap Python tutorial search](https://www.youtube.com/results?search_query=OpenWeatherMap+API+Python+tutorial)
