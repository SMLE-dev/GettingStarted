import time

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print(f"{seconds} seconds remaining")
    time.sleep(1)
    seconds -= 1

print("Time's up!")