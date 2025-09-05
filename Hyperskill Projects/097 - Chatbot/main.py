def greet(bot_name: str, birth_year: str) -> None:
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name() -> None:
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age() -> None:
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainders = [int(input()) for _ in range(3)]
    coefficients = [70, 21, 15]
    age = sum(r * c for r, c in zip(remainders, coefficients)) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count() -> None:
    print('Now I will prove to you that I can count to any number you want.')
    number = int(input())
    for i in range(number + 1):
        print(f'{i}!')


def test() -> None:
    print("Let's test your programming knowledge.")
    question = """\
Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program."""
    print(question)
    correct_answer = '2'
    while input() != correct_answer:
        print('Please, try again.')


def end() -> None:
    print('Congratulations, have a nice day!')


def main() -> None:
    greet('Aid', '2020')
    remind_name()
    guess_age()
    count()
    test()
    end()


if __name__ == '__main__':
    main()