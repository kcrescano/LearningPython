# mine
guest = []
while True:
    guest.append(input())
    if guest[-1] == '.':
        guest.pop()
        print(guest, len(guest), sep='\n')
        break
# Hyperskill user posted solutions
names = list(iter(input, '.'))
print(names)
print(len(names))
# Hyperskill user posted solutions
guest = []
while '.' not in guest:
    guest.append(input())
print(guest[:-1], len(guest) - 1, sep='\n')
