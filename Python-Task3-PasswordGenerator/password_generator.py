import random
import string


def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def validate_password(password, use_uppercase, use_digits, use_symbols):
    if use_uppercase and not any(char.isupper() for char in password):
        return False

    if use_digits and not any(char.isdigit() for char in password):
        return False

    if use_symbols and not any(char in string.punctuation for char in password):
        return False

    return True


print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter minimum password length: "))

        if length <= 0:
            print("Error: Password length must be greater than 0.")
            continue

        uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        digits = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(
            length,
            uppercase,
            digits,
            symbols
        )

        if validate_password(password, uppercase, digits, symbols):
            print("\nGenerated Password:", password)
        else:
            print("\nError: Generated password does not meet the requirements.")

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("Thank you for using the Password Generator.")
            break

    except ValueError:
        print("Error: Please enter a valid number.")