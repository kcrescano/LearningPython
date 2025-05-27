def create_card():
    card = [["-" for _ in range(50)],
                 *[[*f"|{" " * 48}|"] for _ in range(28)],
                 ["-" for _ in range(50)]]
    card[27] = f"|{"Merry Xmas".center(48, ' ')}|"
    return card

def create_tree(height, interval):
    tree = []
    for i in range(1, height):
        tabs = [*(height - i - 1) * " "]
        stars = [*f"/{(i * 2 - 1) * "*"}\\"]
        tree.append(tabs + stars)
    tree = decorate_tree(tree, interval)
    tree.insert(0, [*(height - 1) * " ", "X"])
    tree.insert(1, [*(height - 1) * " ", "^"])
    tree.append([*(height - 2) * " ", *"| |"])
    return tree

def decorate_tree(tree, interval):
    current_decoration = 1
    for tree_row in tree:
        star_indices = [j for j, char in enumerate(tree_row) if char == '*'][1: -1: 2]
        for i in star_indices:
            if current_decoration == 1:
                tree_row[i] = 'O'
            current_decoration += 1
            if current_decoration > interval:
                current_decoration = 1
    return tree

def insert_tree(card, tree, x, y):
    y -= len(tree) - 3
    for i, row in enumerate(tree):
        for j, char in enumerate(row):
            if char != ' ':
                card[i + x][j + y] = char

    return card

parameters = [int(x) for x in input().split()]
post_card = create_card()

for i in range(0, len(parameters), 4):
    christmas_tree = create_tree(parameters[i], parameters[i + 1])
    try:
        post_card = insert_tree(post_card, christmas_tree, parameters[i + 2], parameters[i + 3])
    except IndexError:
        for row in christmas_tree:
            print("".join(row))
        exit(0)

for row in post_card:
    print("".join(row))
