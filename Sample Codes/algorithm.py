# mine
expression = input()
stack_ = []

for char in expression:
    if char == '(':
        stack_.append(char)
    elif char == ')':
        if stack_:
            if stack_[-1] == '(':
                stack_.pop()
            else:
                stack_.append(char)
        else:
            stack_.append(char)
print("OK" if not stack_ else "ERROR")
# Hyperskill user posted solution
brackets = [1 if x == "(" else -1 for x in input() if x in "()"]
count = 0
while brackets and count <= 0:
    count += brackets.pop()
print("OK" if count == 0 else "ERROR")
# Hyperskill user posted solution
try:
    br = []
    _ = [br.append(b) if b == '(' else br.pop() if b == ')' else 0 for b in input()]
    print('OK' if not br else 'ERROR')
except IndexError:
    print('ERROR')
#**************************************************************************
# mine
def startswith_capital_counter(names):
    return len([name for name in names if name[0].isupper()])
# Hyperskill user posted solution
def startswith_capital_counter(names):
    return sum(name.istitle() for name in names)
# Hyperskill user posted solution
def startswith_capital_counter(names):
    return len(list(filter(lambda x: x.istitle(), names)))
