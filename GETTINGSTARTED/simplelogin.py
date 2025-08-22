USERNAME = "admin"
PASSWORD = "123456"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print(f"Login successful! Welcome, {username}")
        break
    else:
        attempts -= 1
        print(f"Access denied, incorrect credentials, {attempts} remaining!")

        if attempts == 0:
            print("Account locked! Too many attempts")