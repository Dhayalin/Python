menu = {"popcorn" : 40,
        "spirit" : 20,
        "nuggets" : 50,
        "puffs" : 20,
        "fries" : 40}

cart = []
total = 0
print("-----------MENU----------")
for key, value in menu.items():
    print(f"{key:20} : {value}")
print("-------------------------")

while True:
    food = input("Enter your Order (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print("The food you selected is not in the Menu")
    elif menu.get(food) is not None:
        cart.append(food)

print("--------Your Order--------")
for item in cart:
    total += menu.get(item)
    print(f"{item:20} : {menu.get(item)}")
print("--------------------------")
print(f"Total is rupees {total}")    
    
