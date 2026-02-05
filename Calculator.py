print("Calculator Program:-")
print(" +  : Addition")
print(" -  : Subtraction")
print(" *  : Multiplication")
print(" %  : Division (Remainder)")
print(" /  : Division (Quotient)")
operator = input("Enter the operation you want to perform: ")

if operator == "+" :
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    result = a + b 
    print(f"Addition of {a} and {b} is {result}")

elif operator == "-" :
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    result = a - b 
    print(f"Subtraction of {a} and {b} is {result}")

elif operator == "*" :
    a = int(input("Enter the 1st value: ")) 
    b = int(input("Enter the 2nd value: "))
    result = a * b 
    print(f"Multiplication of {a} and {b} is {result}")

elif operator == "+" :
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    result = a + b 
    print(f"Addition of {a} and {b} is {result}")

elif operator == "%" :
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    if b == 0:
        print("Division By zero is not possible")
    elif b < 0:
        print("Division By Division by negative integers is not possible")
    else:        
        result = a % b 
        print(f"Division (Remainder) of {a} and {b} is {result}")

elif operator == "/" :
    a = int(input("Enter the 1st value: "))
    b = int(input("Enter the 2nd value: "))
    if b == 0:
        print("Division By zero is not possible")
    elif b < 0:
        print("Division By Division by negative integers is not possible")
    else:      
        result = a / b 
        print(f"Division (Quotient) of {a} and {b} is {result}")

else:
    print("Invalid Operation")
    