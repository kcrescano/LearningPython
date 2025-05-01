#mine
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
print("Correct" if input() in dictionary else "Incorrect")
# hyperskill user posted solution
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
print(["Incorrect", "Correct"][input() in dictionary])
#**************************************************************************
#mine
print([x for x in range(1, 1000) if x % 3 == 0])
# hyperskill user posted solution
print(list(range(3, 1000, 3)))
#**************************************************************************
#mine
stack = []
for _ in range(int(input())):
    action = input().split()
    if action[0] == "PUSH":
        stack.append(action[1])
    else:
        stack.pop()

print(*stack[::-1], sep='\n')
# hyperskill user posted solution
my_stack = []
for _ in range(int(input())):
    try:
        action, value = input().split(' ')
        my_stack.append(value)
    except ValueError:
        my_stack.pop()
print(*my_stack[::-1], sep='\n')
