import random


def get_winning_choices(choices):
    wc = {}
    for i in range(len(choices)):
        wc[choices[i]] = []
        for j in range(1, len(choices) // 2 + 1):
            wc[choices[i]].append(choices[(i + j) % len(choices)])
    return wc


available_choices = ["rock", "paper", "scissors"]

print("Enter your name: ", end="")
name = input()
print(f"Hello, {name}")
file_name = "rating.txt"
choices_ = input().strip()
if choices_ != "":
    available_choices = choices_.split(",")

winning_choices = get_winning_choices(available_choices)
print(available_choices)
print(winning_choices)

rating = 0
if file_name:
    with open(file_name, "r") as file:
        for line in file:
            user, rating = line.split()
            if user == name:
                rating = int(rating)
                break

print("Okay, let's start")

while True:
    user_choice = input().strip().lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice in available_choices:
        if user_choice == computer_choice:
            print(f"There is a draw ({user_choice})")
            rating += 50
        elif computer_choice in winning_choices[user_choice]:
            print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
    elif user_choice == "!rating":
        print(f"Your rating: {rating}")
    elif user_choice == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
        rating = 0
