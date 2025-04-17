# mine
string = input().lower()
for char in ',.!?':
    string = string.replace(char, '')
print(string)
# Hyperskill user posted solutions
print(''.join([i for i in input() if i not in ',.!?']).lower())
# Hyperskill user posted solutions
import re
print(re.sub('[,.!?]', '', input()).lower())
#**************************************************************************
# mine
print(*"You are the best programmer!".split(), sep='\n')
# Hyperskill user posted solutions
print('\n'.join("You are the best programmer!".split()))
# Hyperskill user posted solutions
print("You are the best programmer!".replace(" ", "\n"))
#**************************************************************************
# mine
text = input().strip().split()
text = [word.capitalize() for word in text]
text[0] = text[0].lower()
print(*text, sep='')
# Hyperskill user posted solutions
sentence = input().title().split()
print(sentence[0].lower() + "".join(sentence[1:]))
# Hyperskill user posted solutions
text = "".join(input().title().split())
print(text[:1].lower() + text[1:])
