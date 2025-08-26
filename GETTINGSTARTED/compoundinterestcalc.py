principle = 0
rate = 0
time = 0

while True:
        principle = float(input("Enter the principle amount: "))
        if principle < 0:
            print("Principle cannot be less than zero")
        else:
            break
while True:
        rate = float(input("Enter the interest rate: "))
        if rate < 0:
            print("interest rate cannot be less than zero")
        else:
            break

while True:
        time = int(input("Enter the time: "))
        if time < 0:
            print("Time cannot be less than zero")
        else:
            break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Your compound interest after {time} year/s is Ksh{total:.2f}")
