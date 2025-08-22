name = str(input("Enter your name: "))

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    gross_income = get_numeric_input("Please enter your monthly income: ")
    expenses = get_numeric_input("Please enter your monthly expenses: ")
    net_income = gross_income - expenses

    if net_income == 0:
        print(f"{name}, you broke even. Your net income is {net_income}")
    elif net_income < 0:
        print(f"{name}, you overspent. Your net income is {net_income}")
    else:
        print(f"{name}, you made a profit. Net income of {net_income}")


    #prompt to continue or quit

    to_continue = input("Would you like to continue to another month?(yes / no): ").lower()
    if to_continue != "yes":
        print("Goodbye!")
        break
