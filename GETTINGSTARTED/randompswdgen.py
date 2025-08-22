import random
import string

while True:
    try:
        password_length = int(input("Enter password length: "))

        if password_length <= 0:
            print("Please enter a number greater than 0")
            continue

    except ValueError:
        print("Please enter a valid number: ")
        continue

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(password_length):
        next_character = random.choice(chars)
        password += next_character

    print(f"Your password is: {password}")

    if input("Would you like to generate a new password (y / n)? ").lower() == "n":
        break
    else:
        continue