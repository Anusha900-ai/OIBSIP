"""Beginner command-line BMI calculator."""


def read_positive_number(prompt):
    """Keep asking until the user enters a number greater than zero."""
    while True:
        answer = input(prompt)

        try:
            value = float(answer)
        except ValueError:
            print("Please enter a number, such as 62.5.")
            continue

        if value <= 0:
            print("Please enter a value greater than zero.")
            continue

        return value


def classify_bmi(bmi):
    """Return the category for a BMI value using the task's ranges."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    print("BMI Calculator")
    weight_kg = read_positive_number("Enter your weight in kilograms: ")
    height_m = read_positive_number("Enter your height in metres: ")

    bmi = weight_kg / (height_m ** 2)
    category = classify_bmi(bmi)

    print(f"Your BMI is {bmi:.2f}.")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
