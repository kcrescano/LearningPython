# mine
def letters(word):
    for i in word:
        yield i
# Hyperskill user posted solution
def letters(word):
    yield from word
#************************************************************************** 
# mine
n = int(input())
def even(num):
    yield num * 2
for i in range(n):
    print(next(even(i)))
# Hyperskill user posted solution
n = int(input())
def even():
    yield from range(0, 2 * n, 2)
print(*even(), sep="\n")
