 def xmas_post_card(*args):
    if len(args) == 2:
        tree = xmastree(args[0], args[1])

        for row in range(len(tree)):
            for column in range(len(tree[row])):
                print(tree[row][column], end="")
            print()
    else:
        post_card = []
        for row in range(30):
            post_card.append([])
            for column in range(50):
                if row in [0, 29]:
                    post_card[row].append('-')
                elif column in [0, 49]:
                    post_card[row].append('|')
                else:
                    post_card[row].append(' ')

        for param in range(0, len(args), 4):
            height, interval, y, x = args[param], args[param+1], args[param+2], args[param+3]
            tree = xmastree(height, interval)
            for row in range(len(tree)):
                for column in range(len(tree[row])):
                    if tree[row][column] != ' ':
                        post_card[row + y][column + (x - height + 1)] = tree[row][column]

        post_card_message(post_card, "Merry Xmas")
        for row in range(30):
            for column in range(50):
                print(post_card[row][column], end="")
            print()


def xmastree(height, interval):
    tree = [[], []]
    if height >= 3 and interval > 0:
        for _ in range(height - 1):
            tree[0].append(" ")
            tree[1].append(" ")

        tree[0].append("X")
        tree[1].append("^")

        interval_counter = 0
        for row in range(1, height):
            tree.append([])
            for _ in range(height - row - 1):
                tree[row + 1].append(' ')
            tree[row + 1].append('/')

            for decor_spot in range(row * 2 - 1):
                if decor_spot % 2 == 0:
                    tree[row + 1].append("*")
                else:
                    if interval_counter % interval == 0:
                        tree[row + 1].append("O")
                    else:
                        tree[row + 1].append("*")
                    interval_counter += 1
            tree[row + 1].append('\\')

        tree.append([])
        for _ in range(height - 2):
            tree[height + 1].append(' ')
        tree[height + 1].append('|')
        tree[height + 1].append(' ')
        tree[height + 1].append('|')

    return tree


def post_card_message(post_card, message):
    message = list(message)
    for column in range(len(message)):
        left_center = int((len(post_card[26]) - len(message)) / 2) - 1
        post_card[27][column + left_center + 1] = message[column]
    return post_card


arguments = [int(x) for x in input().split(" ")]
xmas_post_card(*arguments)
