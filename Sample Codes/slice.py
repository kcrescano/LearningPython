# mine
ticket = [int(x) for x in input()]
half1 = sum(ticket[:3])
half2 = sum(ticket[3:])

if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")

# hyperskill user posted solution
ticket = [int(x) for x in input()]
print(sum(ticket[:3]) == sum(ticket[-3:]) and "Lucky" or "Ordinary")
