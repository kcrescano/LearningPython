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
