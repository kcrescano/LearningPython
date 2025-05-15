# mine
for a, b in zip(v1, v2):
    print(a + b)
# Hyperskill user posted solution
for e in zip(v1, v2):
    print(sum(e))
#**************************************************************************
# mine
for i, name in enumerate(student_list, start=1):
    print(i, name)
# Hyperskill user posted solution
for student in enumerate(student_list, start=1):
    print(*student)
