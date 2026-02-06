import random

num = random.randint(1,100)

guesses = 0
is_running = True

print("Number Guessing Game:-")
print("Select a number Between 1 and 100")

while is_running:
    guess = input("Enter your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < 1 or guess > 100:
            print("Enter your guess within the range of 1 to 100")
        elif guess < num:
            print("Too low. Try again")
        elif guess > num:
            print("Too high. Try again")
        else:
            print("Your Guess is Correct")
            print(f"The Answer is {num}")
            print(f"Number of guesses is {guesses}")
            is_running = False
    
    else:
        print("Enter Only Numbers!")
