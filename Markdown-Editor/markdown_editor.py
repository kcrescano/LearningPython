def header():
    global markdown_file
    level = int(input("Level: "))
    while level > 6 or level < 1:
        print("The level should be within the range of 1 to 6")
        level = int(input("Level: "))
    text = input("Text:")
    markdown_file += f"{'#' * level} {text}\n"
    print(markdown_file)

def plain():
    global markdown_file
    text = input("Text:")
    markdown_file += text
    print(markdown_file)

def bold():
    global markdown_file
    text = input("Text:")
    markdown_file += f"**{text}**"
    print(markdown_file)

def italic():
    global markdown_file
    text = input("Text:")
    markdown_file += f"*{text}*"
    print(markdown_file)
    
def link():
    global markdown_file
    label = input("Label:")
    url = input("URL:")
    markdown_file += f"[{label}]({url})"
    print(markdown_file)
    
def inline_code():
    global markdown_file
    text = input("Text:")
    markdown_file += f"`{text}`"
    print(markdown_file)
    
def ordered_list():
    global markdown_file
    rows = int(input("Number of rows:"))
    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows:"))
    for i in range(rows):
        markdown_file += f"{i+1}. {input()}\n"
    print(markdown_file)
    
def unordered_list():
    global markdown_file
    rows = int(input("Number of rows:"))
    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows:"))
    for _ in range(rows):
        markdown_file += f"* {input()}\n"
    print(markdown_file)
    
def new_line():
    global markdown_file
    markdown_file += "\n"
    print(markdown_file)

markdown_file = ''
formatter = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
special_commanad = ["!help", "!done"]

while True:
    choice = input("Choose a formatter: ")
    if choice == "!help":
        print("Available fromatters:", " ".join(formatter))
        print("Special commands:", " ".join(special_commanad))
    elif choice == "!done":
        file = open("output.md", "w", encoding='utf-8')
        file.writelines(markdown_file)
        file.close()
        exit()
    elif choice not in formatter:
        print("Unknown formatting type or command")
    elif choice == "header":
        header()
    elif choice == "plain":
        plain()
    elif choice == "bold":
        bold()
    elif choice == "italic":
        italic()
    elif choice == "link":
        link()
    elif choice == "inline-code":
        inline_code()
    elif choice == "ordered-list":
        ordered_list()
    elif choice == "unordered-list":
        unordered_list()
    elif choice == "new-line":
        new_line()
