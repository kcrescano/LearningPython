import random

print('Enter your name:', end=' ')
name = input()
print(f'Hello, {name}')

score = int(dict(line.split() for line in open('rating.txt')).get(name, '0'))
options = input().split(',')
if not options[0]: options = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    choice = input()
    if choice == '!exit': print('Bye!'); break
    if choice == '!rating': print(f'Your rating: {score}'); continue
    if choice not in options: print('Invalid input'); continue

    comp = random.choice(options)
    if choice == comp:
        print(f'There is a draw ({comp})')
        score += 50
    else:
        idx = options.index(choice)
        others = options[idx+1:] + options[:idx]
        mid = len(others)//2
        if comp in others[mid:]:
            print(f'Well done. The computer chose {comp} and failed')
            score += 100
        else:
            print(f'Sorry, but the computer chose {comp}')
