# mine
print(type("int"))
print(type(394))
print(type(2.12))

# hyperskill user posted solution
for i in 'int', 394, 2.71:
    print(type(i))
#**************************************************************************
# mine
print("1 2 3 4 5 6 7 8 9 10")

# hyperskill user posted solution
print(*range(1, 11))

#**************************************************************************
# mine
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for char in string:
    if char in vowels:
        count += 1
print(count)

# hyperskill user posted solution
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
print(sum(vowel in vowels for vowel in string))
