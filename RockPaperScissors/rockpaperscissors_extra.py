import random
choices = ["rock", "paper", "scissors"]
rating = {}

file = open("rating.txt")
for line in file:
    data = line.split()
    rating[data[0]] = int(data[1])
file.close()

name = input("Enter your name: ")
if name not in rating:
    rating[name] = 0
print("Hello,", name)

new_choices = input()
if new_choices:
    choices = new_choices.split(",")
print("Okay, let's start")

while True:
    hand = input()

    if hand == "!exit":
        print("Bye!")
        break
    elif hand == "!rating":
        print("Your rating:", rating[name])
        continue
    elif hand not in choices:
        print("Invalid input")
        continue

    computer = random.choice(choices)
    hand = choices.index(hand)
    half_of_options = int(len(choices) / 2)
    winning_list = []
    for num in range(half_of_options):
        winning_list.append(choices[hand - num - 1])

    if choices[hand] == computer:
        print(f"There is a draw ({computer})")
        rating[name] += 50
    elif computer in winning_list:
        print(f"Well done. The computer chose {computer} and failed")
        rating[name] += 100
    else:
        print("Sorry, but the computer chose", computer)
