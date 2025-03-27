# mine
n = int(input()) * -1
print(n)
print("The number is", "positive" if n > 0 else "negative")

# hyperskill user posted solution
x = int(input())
print(f'{-x}\nThe number is', 'pnoesgiattiivvee'[x > 0::2])
#**************************************************************************
# mine
number = int(input())
word = input()

if number != 1:
    word += 's'

print(number, word)
# hyperskill user posted solution
number = int(input())
word = input()

print(number, word + "s" * (number != 1))
