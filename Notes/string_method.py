string = "Hello" or 'World' or "101"

message = "bonjour and welcome to Paris!"

print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
# `message` is not changed
print(message)  # bonjour and welcome to Paris!

title_message = message.title() 
# `title_message` contains a new string 
# with the first character of each word capitalized
print(title_message)  # Bonjour And Welcome To Paris!

print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)
print(replaced_message)  # b!nj!ur and welcome to Paris!

# again, the source string is unchanged, only its copy is modified
print(message)  # bonjour and welcome to Paris!

word = "Mississippi"

# starting from the right side, all "i", "p", and "s" are removed:
print(word.rstrip("ips"))  # "M"

# the word starts with "M" rather than "i", "p", or "s", so no chars are removed from the left side:
print(word.lstrip("ips"))  # "Mississippi"

# "M", "i", "p", and "s" are removed from both sides, so nothing is left:
print(word.strip("Mips"))  # ""
