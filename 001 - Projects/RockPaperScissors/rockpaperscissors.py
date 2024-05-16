import random
choices = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    hand = input()
    computer = random.choice(list(choices.keys()))

    if hand == "!exit":
        print("Bye!")
        break
    elif hand not in choices:
        print("Invalid input")
    elif choices[hand] == computer:
        print(f"Well done. The computer chose {computer} and failed")
    elif choices[computer] == hand:
        print("Sorry, but the computer chose", computer)
    elif hand == computer:
        print(f"There is a draw ({hand})")
    else:
        print("Invalid input")
