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
