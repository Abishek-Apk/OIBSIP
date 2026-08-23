def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("===== BMI CALCULATOR =====")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")
            continue

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print("\n===== RESULT =====")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

        break

    except ValueError:
        print("Error: Please enter valid numeric values.")