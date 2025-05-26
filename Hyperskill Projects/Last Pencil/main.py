print("How many pencils would you like to use: ")
while True:
    try:
        pen = int(input())
        if pen < 1:
            print("The number of pencils should be positive")
        else:
            break
    except ValueError:
        print("The number of pencils should be numeric")

print("Who will be the first (John, Jack): ")
while (player := input()) not in ["John", "Jack"]:
    print("Choose between 'John' and 'Jack'")

while pen > 0:
    print(pen * '|')
    print(f"{player}'s turn!")

    while True:
        try:
            num = int(input())
            if num < 1 or num > 3:
                print("Possible values: '1', '2' or '3'")
                continue
            if num > pen:
                print("Too many pencils were taken")
                continue
            break
        except ValueError:
            print("Possible values: '1', '2' or '3'")

    pen -= num
    player = 'Jack' if player == 'John' else 'John'

print(f"{player} won!")
