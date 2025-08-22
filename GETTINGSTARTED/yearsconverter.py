YEARS_TO_DAYS = 365
DAYS_TO_YEARS = 1 / 365

duration = input("Enter type of duration(Y / D ): ")

if duration == "Y":
    duration = float(input("Enter number of year(s): "))
    duration = duration * YEARS_TO_DAYS
    print(f"The duration is equivalent to: {duration} day(s)")
elif duration == "D":
    duration = int(input("Enter number of day(s): "))
    duration = duration / 365
    print(f"The duration is equivalent to: {duration} year(s)")
else:
    print(f"{duration} is invalid")