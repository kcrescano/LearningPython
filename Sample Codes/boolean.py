# mine
def check_values(first_value, second_value):
    return bool(first_value) and bool(second_value)
# Hyperskill user posted solution
def check_values(first_value, second_value):
    return all([first_value, second_value])
#************************************************************************** 
# mine
def print_book_info(title, author=None, year=None):
    book = f'"{title}"'
    if author or year:
        book += ' was written'
    if author:
        book += f' by {author}'
    if year:
        book += f' in {year}'
    print(book)
# Hyperskill user posted solution
def print_book_info(title, author=None, year=None):
    print(f"\"{title}\"", " was written" if author or year else "",
          f" by {author}" if author else "",
          f" in {year}" if year else "", sep="")
# Hyperskill user posted solution
def print_book_info(title, author=None, year=None):
    print(f'"{title}"', ' was written' * bool(author or year), 
          f' by {author}' * bool(author),
          f' in {year}' * bool(year), sep='')
