temp = float(input("Enter the Temperature: "))
unit = input("Is this temperature in Celsius or in Farenheit (C/F): ")

if unit == "C":
    temp_new = (temp * 9/5) + 32
    print(f"Temperature in Celsius: {temp}")
    print(f"Temperature in fahrenheit: {temp_new}")

elif unit == "F":
    temp_new = (temp - 32) * 5/9
    print(f"Temperature in fahrenheit: {temp}")
    print(f"Temperature in Celsius: {temp_new}")

else:
    print("Invalid Unit")