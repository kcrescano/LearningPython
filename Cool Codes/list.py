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
