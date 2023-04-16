import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
#list = collection of elements, multiple strings stored in it
#options[0]
#option 0 is "rock", 1 is "paper", -1 is "scissors", ...

while True:
    user_input = input("Type Rock/Paper/Scissors or Q for quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #generate a random number from 0 to 2
    #rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    #the "," adds a space the "+" not

    if user_input == "rock" and computer_pick == "scissors":
        print("you won. you'll see next time")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won. you'll see next time")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won. you'll see next time")
        user_wins += 1

    else: 
        print("you lost! ha!")
        computer_wins += 1
        continue

print("you won", user_wins, "times.")
print("I won", computer_wins, "times.")
print("bye!")


#Date: 15.04.23
#Sources: https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=6&t=1486s