# Write your code here
import json
import os
import random
import sys


def check_input(message, input_):
    while True:
        if message == 'input_term' and input_ in flash_card.keys():
            input_ = input_log(f'The card "{input_}" already exists. Try again:\n')
        elif message == 'input_definition' and input_ in [item[0] for item in flash_card.values()]:
            input_ = input_log(f'The definition "{input_}" already exists. Try again:\n')
        else:
            break
    return input_


def input_log(message=''):
    user_input = input(message)
    log.append(message)
    log.append(user_input)
    return user_input


def print_log(message):
    print(message)
    log.append(message)


def add_card():
    term = check_input('input_term', input_log('The card:\n'))
    definition = check_input('input_definition', input_log('The definition for card:\n'))
    flash_card[term] = [definition, 0]
    print_log(f'The pair ("{term}":"{definition}") has been added.')


def remove_card():
    card = input_log('Which card?\n')
    try:
        flash_card.pop(card)
        print_log('The card has been removed.')
    except KeyError:
        print_log(f'Can\'t remove "{card}": there is no such card.')


def import_card(initialize=False):
    file = import_file if initialize else (file := input_log('File name:\n'))
    if os.path.isfile(file):
        with open(file, 'r') as f:
            cards = json.loads(f.readline())
            flash_card.update(cards)
            print_log(f'{len(flash_card)} cards have been loaded.')
    else:
        print_log('File not found.')


def export_card():
    with open(export_file if export_file else input_log('File name:\n'), 'w') as f:
        f.write(json.dumps(flash_card))
    print_log(f'{len(flash_card)} cards have been saved.')


def ask_card():
    n = input_log('How many times to ask?')
    for i in range(int(n)):
        term, definition = random.choice(list(flash_card.items()))
        if (definition_ := input_log(f'Print the definition of "{term}"\n')) == definition[0]:
            print_log('Correct!')
        else:
            flash_card[term][1] += 1
            if definition_ in [item[0] for item in flash_card.values()]:
                msg = f'Wrong. The right answer is "{definition[0]}", '
                right_term = [term_[0] for term_ in flash_card.items() if definition_ == term_[1][0]]
                msg += f'but your definition is correct for "{right_term[0]}".'
                print_log(msg)
            else:
                print_log(f'Wrong. The right answer is "{definition[0]}".')


def save_log():
    with open(input_log('File name:\n'), 'w') as f:
        for item in log:
            f.write(f'{item}\n')
    print_log('The log has been saved.')


def hardest_card():
    if flash_card:
        hard_card = sorted(flash_card.items(), key=lambda x: -x[1][1])[0]
        if hard_card[1][1] != 0:
            print_log(f'The hardest card is "{hard_card[0]}". You have {hard_card[1][1]} errors answering it.')
        else:
            print_log('"There are no cards with errors."')
    else:
        print_log('"There are no cards with errors."')


def reset_stats():
    print_log('Card statistics have been reset.')
    for card in flash_card.items():
        card[1][1] = 0


command = {'add': lambda: add_card(),
           'remove': lambda: remove_card(),
           'import': lambda: import_card(),
           'export': lambda: export_card(),
           'ask': lambda: ask_card(),
           'log': lambda: save_log(),
           'hardest card': lambda: hardest_card(),
           'reset stats': lambda: reset_stats(),}
flash_card = {}
log = []

export_file = ''
if len(sys.argv) > 1:
    parameters = sys.argv[1:]
    for param in parameters:
        cmd, filename = param.split('=')
        if cmd == '--export_to':
            export_file = filename
        if cmd == '--import_from':
            import_file = filename
            import_card(True)

while True:
    print_log('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
    if (cmd := input_log()) != 'exit':
        command[cmd]()
    else:
        print_log('Bye bye!')
        if export_file:
            export_card()
        exit()
    print()
