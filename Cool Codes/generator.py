# mine
def letters(word):
    for i in word:
        yield i
# Hyperskill user posted solution
def letters(word):
    yield from word
