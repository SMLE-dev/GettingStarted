def get_valid_name():
    """Get a valid name from user input"""
    while True:
        name = input("Please enter your name: ").strip()
        if name and name.replace(" ", "").isalpha():
            print(f"Welcome, {name}!")
            return name
        else:
            print("Please enter a valid name (letters and spaces only).")

def get_valid_age():
    """Get a valid age from user input"""
    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            age_int = int(age)
            if 1 <= age_int <= 120:
                print(f"You are {age} years old.")
                if age_int < 18:
                    print("Nice one.")
                else:
                    print("You're welcomed.")
                return age_int
            else:
                print("Please enter a realistic age (1-120).")
        else:
            print("Please enter a valid number for age.")

def get_income_level():
    """Get income level selection from user"""
    options = ["1 (under 30,000 KSH)", "2 (30,000 - 100,000 KSH)", "3 (Over 100,000 KSH)"]
    print("How much revenue did you generate? Choose from the following options:")
    for option in options:
        print(f"  {option}")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice in ["1", "2", "3"]:
            print(f"Your income level is {choice}.")
            if choice == "1":
                print("You're a smart entrepreneur building your empire!")
            elif choice == "2":
                print("You're a successful business professional on the rise!")
            else:
                print("You're an exceptional business leader at the top!")
            return choice
        else:
            print("Please enter 1, 2, or 3.")

def calculate_tax(income):
    """Calculate tax based on simple brackets"""
    if income <= 30000:
        return income * 0.05
    elif income <= 100000:
        return income * 0.10
    else:
        return income * 0.20

def get_valid_float(prompt, field_name):
    """Get a valid float input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print(f"Please enter a non-negative number for {field_name}.")
        except ValueError:
            print(f"Please enter a valid number for {field_name}.")

def save_to_file(filename, data):
    """Save financial summary to a file"""
    with open(filename, "w") as file:
        file.write(data)
    print(f"Summary saved to {filename}")

def main():
    """Main function to run the financial data collection"""
    print("=== Financial Data Collection System ===\n")

    # Get user information
    name = get_valid_name()
    age = get_valid_age()

    # Get income level selection
    get_income_level()

    # Get gross income
    gross_income = get_valid_float("Please enter your gross income: ", "gross income")
    print(f"Your gross income is ksh{gross_income:,.2f}.")

    if gross_income < 30000:
        print("You're a smart entrepreneur building your empire!")
    elif gross_income < 100000:
        print("You're a successful business professional on the rise!")
    else:
        print("You're an exceptional business leader at the top!")

    # Get financial data
    print("\n--- Financial Details ---")
    revenue = get_valid_float("Please enter your revenue: ", "revenue")
    utilities = get_valid_float("Please enter your utilities: ", "utilities")
    cogs = get_valid_float("Please enter your COGS (Cost of Goods Sold): ", "COGS")
    other_expenses = get_valid_float("Please enter your other expenses: ", "other expenses")

    # Calculate totals
    total_expenses = utilities + cogs + other_expenses
    net_profit = revenue - total_expenses
    tax = calculate_tax(net_profit)
    net_income_after_tax = net_profit - tax

    # Display results
    print("\n=== Financial Summary ===")
    print(f"Revenue: ksh{revenue:,.2f}")
    print(f"Total Expenses: ksh{total_expenses:,.2f}")
    print(f"  - Utilities: ksh{utilities:,.2f}")
    print(f"  - COGS: ksh{cogs:,.2f}")
    print(f"  - Other Expenses: ksh{other_expenses:,.2f}")
    print(f"Net Profit: ksh{net_profit:,.2f}")
    print(f"Tax: ksh{tax:,.2f}")
    print(f"Net Income After Tax: ksh{net_income_after_tax:,.2f}")

    if net_profit > 0:
        print("Congratulations! You have a positive net profit.")
    elif net_profit < 0:
        print("You have a net loss. Consider reviewing your expenses.")
    else:
        print("You broke even this period.")

    # Save summary to file
    summary = (
        f"Name: {name}\nAge: {age}\nGross Income: ksh{gross_income:,.2f}\n"
        f"Revenue: ksh{revenue:,.2f}\nTotal Expenses: ksh{total_expenses:,.2f}\n"
        f"  - Utilities: ksh{utilities:,.2f}\n"
        f"  - COGS: ksh{cogs:,.2f}\n"
        f"  - Other Expenses: ksh{other_expenses:,.2f}\n"
        f"Net Profit: ksh{net_profit:,.2f}\n"
        f"Tax: ksh{tax:,.2f}\n"
        f"Net Income After Tax: ksh{net_income_after_tax:,.2f}\n"
    )
    save_to_file("financial_summary.txt", summary)

if __name__ == "__main__":
    main()
    




