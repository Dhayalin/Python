def show_balance(balance):
    print(f"Your Balance is Rupees {balance:.2f}")


def deposit(balance):
    try: 
        amount = float(input("Enter the Amount to Deposit: "))
    except ValueError:
        print("Enter a Valid Amount in Numbers!")
        return balance
    if amount <= 0:
        print("Enter a Valid Amount!")
        return balance
    else:
        return balance + amount


def withdraw(balance):
    try:
        amount = float(input("Enter the Amount to Withdraw: "))
    except ValueError:
        print("Enter a Valid Amount in Numbers!")
        return balance
        
    if amount <=0:
        print("Enter a Valid Amount!")
        return balance
    elif amount > balance:
        print("Your Withdrawal Amount is more than the balance you have!")
        return balance
    else:
        return balance - amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("--------Banking Program--------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your Choice (1 to 4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Enter a valid Choice!...")                

    print("Thank you! for Banking")
    print("Have a Nice Day!")


if __name__ == '__main__':
    main()