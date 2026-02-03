weight = float(input("Enter your weight: "))
unit = input("Is this weight is in Kgs or pounds: ")


if unit == "Kgs":
    weight1 = weight * 2.205
    print(f"Your weight in Kgs is {weight}")
    print(f"Your weight in Pounds is {round(weight1), 3}")
else:
    weight1 = weight / 2.205
    print(f"Your weight in Pounds is {weight}")
    print(f"Your weight in Kgs is {round(weight1)}")