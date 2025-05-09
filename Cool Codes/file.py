# mine
with open('animals.txt', 'r', encoding='utf-8') as file:
    animals = file.readlines()
with open('animals_new.txt', 'w', encoding='utf-8') as file:
    for animal in animals:
        file.write(animal.replace('\n', ' '))
# Hyperskill user posted solution
with open('animals.txt', 'r') as old_file, open('animals_new.txt', 'w') as new_file:
    for animal in old_file.readlines():
        new_file.write(animal.replace('\n', ' '))
# Hyperskill user posted solution
open("animals_new.txt", "w").write(" ".join(open("animals.txt").read().split()))
