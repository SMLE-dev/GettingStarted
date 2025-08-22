foods = []
prices = []
total = 0

while True:
    food = input("Enter food you would like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: ksh"))
        foods.append(food)
        prices.append(price)

print("----MY CART----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ksh{total}")