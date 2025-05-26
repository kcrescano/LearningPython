import re

def valid_name(*names):
    for name in names:
        print(name)
        if len(name) < 2 or not name.replace("'", "").replace("-", '').isalpha():
            return False
    return True

def valid_email(email):
    return re.match(r"\w+@[a-zA-Z\d]+\.[a-zA-Z\d]+", email)

def add_students():
    new_students = {}
    print("Enter student credentials or 'back' to return:")
    while (info := input("")) != 'back':
        try:
            *name, email = info.strip().split()
            if not valid_name(name[:1]):
                print("Incorrect first name")
            elif not valid_name(name[1:]):
                print("Incorrect last name")
            elif not valid_email(email):
                print("Incorrect email")
        except ValueError:
            print("Incorrect credentials.")
        else:
            print("The students has been added.")
            new_students[email] = (name[:1], " ".join(name[1:]))

    print(f"Total {len(new_students)} students have been added.")
    return new_students

student_list = {}

print("Learning progress tracker")
while (cmd := input().strip()) != "exit":
    match cmd.lower():
        case "add students":
            student_list.update(add_students())
        case "":
            print("No input.")
        case "back":
            print("Enter 'exit' to exit the program.")
        case _:
            print("Error: unknown command!")
print("Bye!")
