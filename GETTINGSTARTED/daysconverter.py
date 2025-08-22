def convert_days(number_of_days):
    hours = number_of_days * 24
    minutes = number_of_days * 24 * 60
    seconds = number_of_days * 24 * 60 * 60

    print(f"{number_of_days} day(s) is equal to: ")
    print(f"{round(hours, 2)} hour(s)")
    print(f"{round(minutes, 2)} minute(s)")
    print(f"{round(seconds, 2)} second(s)")

while True:
    try:
        days = float(input("Enter the number of days (or '0' to quit): "))
        if days == 0:
            print("Goodbye have a nice time!")
            break
        convert_days(days)
    except ValueError:
        print("Enter a valid number: ")