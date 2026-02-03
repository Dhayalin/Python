print("----Welcome To Foodie Spot----")
print("Menu:")
print("1.Chicken Fried Rice - 120")
print("2.Chicken Noodles - 120")
print("3.Chicken Briyani - 110")
print("4.Mutton Briyani - 130")
print("5.Egg Briyani - 100")
print("Choose your Order.............")

foods = []
prices = []
total = 0

while True:
    item = input("Enter your Order (press q to quit): ")
    if item == "q":
        break
    else:
        foods.append(item)
        if item == "Chicken Fried Rice":
            prices.append(120)
        elif item == "Chicken Noodles":
            prices.append(120)                
        elif item == "Chicken Briyani":
            prices.append(110)
        elif item == "Mutton Briyani":
            prices.append(130)
        elif item == "Egg Briyani":
            prices.append(100)


print("Your Order is: ")
for food in foods:
    print(food, end=" ")
print("Total Amount is:")    
for price in prices:
    total += price
print(total)                    