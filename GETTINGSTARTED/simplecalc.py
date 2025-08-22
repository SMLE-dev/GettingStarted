 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

print("simple calculator")

while True:
    print("select operation: ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")

    choice = input("enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("invalid input")
        print("please enter a valid choice")
        print("restart the program")
        
    
        
            
    
    
     

