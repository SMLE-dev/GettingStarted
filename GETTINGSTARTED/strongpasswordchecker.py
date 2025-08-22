import string

print("Password strength checker")
print("Password must contain at least 8 characters")
print("Password must contain special characters")
print("Password must contain numbers")

while True:
    password = input("\nEnter password: ")

    length_ok = len(password) >= 8
    special_ok = any(char in string.punctuation for char in password)
    number_ok = any(char.isdigit() for char in password)

    if length_ok and special_ok and number_ok:
        print("strong password")
        break
    else:
        print("Weak password")
        if not length_ok:
            print("Password must contain at least 8 characters")
        if not special_ok:
            print("Password must contain special characters")
        if not number_ok:
            print("Password must contain numbers")