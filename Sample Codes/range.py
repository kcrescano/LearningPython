# mine
a = int(input().strip())
print(a < 10 or a > 250)

# hyperskill user posted solution
a = int(input().strip())
print(a not in range(10, 251))
#**************************************************************************
# mine
class1 = int(input())
class2 = int(input())
class3 = int(input())

desk = 0
desk += class1 // 2 + class1 % 2
desk += class2 // 2 + class2 % 2
desk += class3 // 2 + class3 % 2

print(desk)

# hyperskill user posted solution
print(sum((int(input()) + 1) // 2 for _ in range(3)))
