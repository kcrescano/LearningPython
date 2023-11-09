msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_10, msg_11, msg_12]

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if 1 in [v1, v2] and v3 == '*':
        msg += msg_7
    if 0 in [v1, v2] and v3 in '*+-':
        msg += msg_8
    if msg != '':
        print(msg_9 + msg)

def save_memory(result):
    global memory
    if is_one_digit(result):
        msg_index = 0
        answer = input(msg_[msg_index])
        
        while answer == 'y' and msg_index < 2:
            msg_index += 1
            answer = input(msg_[msg_index])

        if answer == 'y':
            memory = result
    else:
        memory = result

def is_one_digit(v):
    if v > -10 and v < 10 and int(v) == v:
        return True
    return False

memory = 0
result = 0

# write your code here
while True:
    x, oper, y = input(msg_0).split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
        if oper not in '+-*/':
            print(msg_2)
        else:
            check(x, y, oper)
            if oper == '+':
                result = x + y
            if oper == '-':
                result = x - y
            if oper == '*':
                result = x * y
            if oper == '/':
                result = x / y
        print(result)
        if input(msg_4) == 'y':
            save_memory(result)
        if input(msg_5) == 'n':
            break
    except ValueError:
        print(msg_1)
    except ZeroDivisionError:
        print(msg_3)
