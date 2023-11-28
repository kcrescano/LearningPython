# write your code here
import random
mark = 0
level_desc = ["1 - simple operations with numbers 2-9", "2 - integral squares 11-29"]
print(*level_desc, sep="\n")

while True:
    try:
        level = int(input())
        if level not in [1, 2]:
            raise ValueError
        break
    except ValueError:
        print("Incorrect format")
            
for _ in range(5):
    if level == 1:
        x, y = random.randint(2,9), random.randint(2,9)
        equation = {"+": lambda x, y: x + y,
                   "-": lambda x, y: x - y,
                   "*": lambda x, y: x * y}
        operand = random.choice(list(equation.keys()))
        answer = equation[operand](x, y)
        print(x, operand, y)
    else:
        square = random.randint(11,29)
        answer = square ** 2
        print(square)
    
    while True:
        try:
            user_input = float(input())
            if user_input == answer:
                mark += 1
                print("Right!")
                break
            else:
                print("Wrong!")
                break
        except ValueError:
            print("Wrong format! Try again.")

save = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
if save in ['y', 'Yes', 'yes', 'YES']:
    name = input("What is your name?")
    print('The results are saved in "results.txt".')
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(f"{name}: {mark}/5 in level {level} ({level_desc[level-1]})")
    file.close()
    
