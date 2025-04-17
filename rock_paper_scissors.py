import random

user_wins = 0
computer_wins = 0

options = ["rock" ,"paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Type Rock/Paper/Scissors")
        continue
    
    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print(f"Computer Picked {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins+=1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins+=1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins+=1
        continue
    else:
        print("You Lost! ")
        computer_wins+=1

print(f"You won {user_wins} times")
print(f"The computer won {computer_wins} times")

print ("GoodBye!")