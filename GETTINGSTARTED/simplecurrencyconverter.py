USD_TO_KSH = 129.23
KSH_TO_USD = 1 / USD_TO_KSH

amount = float(input("Enter amount: "))
currency = input("Enter the currency(USD / KSH): ")

if currency == "KSH":
    amount = amount * KSH_TO_USD
    currency = "USD"
elif currency == "USD":
    amount = amount / USD_TO_KSH
    currency = "KSH"
else:
    print(f"{currency} is not valid.")

print(f"The amount is equivalent to: {round(amount, 2)} {currency}")