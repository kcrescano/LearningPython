def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    print(f'What a great name you have, {input()}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remainder = []
    for i in range(3, 8, 2):
        remainder.append(int(input()))
    age = (remainder[0] * 70 + remainder[1] * 21 + remainder[2] * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    for i in range(int(input()) + 1):
        print(i, '!')


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.''')
    while input() != '2':
        print('Please, try again.')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
