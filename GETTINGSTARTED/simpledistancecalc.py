
print("---Distance converter app---")

distance = float(input("Enter the distance: "))
unit = input("Kilometer or Miles(KM or M)? ")

if unit == "KM":
    distance = distance * 0.621371
    unit = "M"
elif unit == "M":
    distance = distance / 0.621371
    unit = "KM"
else:
    print(f"{unit} is not a valid number.")

print(f"The distance is: {round(distance, 2)} {unit}")