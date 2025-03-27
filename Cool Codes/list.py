#mine
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
print("Correct" if input() in dictionary else "Incorrect")

# hyperskill user posted solution
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
print(["Incorrect", "Correct"][input() in dictionary])
