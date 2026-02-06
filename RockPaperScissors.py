import random
options = ("rock","paper","scissors")
print("Game Of Rock - Paper - Scissors")
is_running = True
count = 0
while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter Your Choice (rock, paper, scissors): ")    

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        count += 1
        print("You Won") 
    elif player == "scissors" and computer == "paper":
        count += 1
        print("You Won")
    elif player == "paper" and computer == "rock":
        count += 1
        print("You Won")
    else:
        count -= 1
        print("You lose")

    do_stop = input("Do you want to Continue (y/n): ").lower()
    if not do_stop == "y":
        is_running = False      

print(f"Your Score is {count}")
print("Thanks for Playing")