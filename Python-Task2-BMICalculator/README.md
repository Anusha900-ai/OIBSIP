# BMI Calculator — Beginner Version

A small command-line Python program that asks for weight in kilograms and height in metres, calculates BMI, and prints the result and category.

## Run it on Windows

1. Open Command Prompt or PowerShell.
2. Go to the folder that contains this README and `bmi_calculator.py`. If you are working from this project repository, run:

   ```powershell
   cd "C:\Users\anush\Documents\Codex\2026-09-30\task-1-voice-assistant-objective-build\outputs\Python-Task2-BMICalculator"
   ```

3. Run the program:

   ```powershell
   python bmi_calculator.py
   ```

4. Enter weight in kilograms and height in metres. For example, enter `60` for 60 kg and `1.65` for 1.65 m.

No extra Python packages are needed for this beginner version.

## How it works

1. `input()` asks the user for text.
2. `float()` converts that text to a decimal number. `try` / `except` catches text that is not a number.
3. The program asks again when a value is not numeric or is zero/negative. Height must be greater than zero to avoid division by zero.
4. It calculates `weight_kg / (height_m ** 2)`. In Python, `** 2` means “squared”.
5. `classify_bmi()` uses `if` conditions to map the result to a category.
6. `:.2f` displays the BMI rounded to two decimal places.

## Category ranges used

- Underweight: BMI below 18.5
- Normal: BMI from 18.5 to below 25
- Overweight: BMI from 25 to below 30
- Obese: BMI 30 or higher

These are the adult categories specified in the project checklist. BMI is a screening measure, not a diagnosis.

## Advanced version roadmap

Build the advanced version in small steps after the command-line program works:

1. Create a window with `tkinter` and add name, weight, and height fields.
2. Add a **Calculate** button that calls the same BMI calculation and category functions.
3. Show the result with a label and set its color based on the category.
4. Create an SQLite table with a user name, weight, height, BMI, category, and date/time. Use Python's built-in `sqlite3` module.
5. Add a user selector and show that user's saved records.
6. Use Matplotlib to plot the selected user's saved BMI values over time.
7. Catch database and graph errors and display a helpful message in the window.

## Learning references

- [Python BMI calculator command-line tutorial search](https://www.youtube.com/results?search_query=Python+BMI+calculator+command+line+tutorial)
- [Official Python tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Official Python sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html)
