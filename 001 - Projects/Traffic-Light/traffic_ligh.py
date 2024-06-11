import os
import threading
import time
from queue import Queue

menu = {1: {'menu': 'Add road', 'action': lambda: add_road()},
        2: {'menu': 'Delete road', 'action': lambda: delete_road()},
        3: {'menu': 'Open system', 'action': lambda: system_menu()},
        0: {'menu': 'Quit', 'action': lambda: end()}, }
state = "menu"
running = True
timer = [0, 0, False]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def end():
    global running
    running = False
    print("Bye!")
    t1.join()
    exit()


def add_road():
    global timer
    road = input("Input road name: ")
    if q.qsize() < roads:
        q.put(road)
        print(f"{road} added")
        if not timer[2]:
            timer[1] = intervals
            timer[2] = True
    else:
        print("Queue is full")
    input()


def delete_road():
    global timer
    if q.qsize():
        road = q.get()
        print(f"{road} deleted")
        timer[0] = timer[0] - 1
        if timer[0] < 0:
            timer[0] = 0
    else:
        print("Queue is empty")
    if not q.qsize():
        timer = [0, 0, False]
    input()


def display_menu():
    print("Menu:")
    for key, item in menu.items():
        print(key, item['menu'], sep=". ")


def get_input(msg):
    input_ = input(msg)
    while True:
        try:
            if int(input_) <= 0:
                raise ValueError
            return int(input_)
        except ValueError:
            input_ = input('Error! Incorrect Input. Try again: ')


def system_menu():
    global state
    state = 'system'
    input()
    state = 'menu'


def system_timer():
    global timer
    while running:

        if state == 'system':
            cls()
            end_timer = time.time()
            print(f'! {int(end_timer - start_timer)}s. have passed since system startup !')
            print(f'! Number of roads: {roads} !')
            print(f'! Interval: {intervals} !', '\n')
            road_timer()
            print(f'\n! Press "Enter" to open menu !')
        if timer[2]:
            if timer[1] == 1:
                timer[1] = intervals
                timer[0] = timer[0] + 1 if timer[0] + 1 < q.qsize() else 0
            else:
                timer[1] -= 1
        time.sleep(1)


def road_timer():
    global timer
    road_list = list(q.queue)
    next_road = timer[0] + 1 if timer[0] + 1 < len(road_list) else 0
    for i in range(len(road_list)):
        if i == timer[0]:
            print(f'Road "{road_list[i]}" will be open for {timer[1]}s.')
        else:
            if next_road == i:
                print(f'Road "{road_list[i]}" will be closed for {timer[1]}s.')
            else:
                print(f'Road "{road_list[i]}" will be closed for {timer[1] + intervals}s.')


print("Welcome to the traffic management system!")
roads = get_input("Input the number of roads: ")
intervals = get_input("Input the interval: ")

q = Queue(maxsize=int(roads))
start_timer = time.time()
t1 = threading.Thread(target=system_timer, name="QueueThread")
t1.start()

while True:
    display_menu()
    try:
        menu[int(input())]['action']()
    except (KeyError, ValueError):
        print('Incorrect option')
        input()
    cls()
