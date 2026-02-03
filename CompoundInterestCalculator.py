principle = float(input("Enter the Principle Amount: "))
while principle <= 0:
    print("Principle can't be zero or a negative value")
    principle = float(input("Enter a Vaild Principle Amount: "))
    
rate_of_interest = int(input("Enter the Interest Rate: "))
while rate_of_interest <= 0:
    print("Rate of Interest can't be zero or a negative value")
    rate_of_interest = int(input("Enter a Vaild Interest Rate: "))

time = int(input("Enter the Time Period: "))
while time <= 0:
    print("Time can't be zero or a negative value")
    time = int(input("Enter a Vaild Time Period: "))

total_amount = principle * pow((1 + rate_of_interest/100),time)

print(f"Principle Amount is {principle}")
print(f"Rate of Interest is {rate_of_interest}")
print(f"Time Period is {time}")
print(f"Total Amount is {total_amount:.2f}")