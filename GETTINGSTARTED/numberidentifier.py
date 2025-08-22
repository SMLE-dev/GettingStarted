print("WELCOME TO NUMBER IDENTIFIER")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number.")

        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print( f"{num} is not a prime number.")

    except ValueError:
        print("Invalid input")

    if input("would you like to continue? (y / n) ").lower() == "n":
        break
    else:
        continue