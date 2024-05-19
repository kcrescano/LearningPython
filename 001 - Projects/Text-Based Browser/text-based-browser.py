import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# write your code here
args = sys.argv
dir_ = args[1]
website = {}
previous = []
tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

if not os.path.exists(dir_):
    os.mkdir(dir_)

while True:
    url = input()
    if url == "exit":
        exit()
    elif url == "back":
        if previous:
            print(website[previous[-2]])
    else:
        if url in website.keys():
            print(website[url])
        elif '.' not in url:
            print("Invalid URL")
        else:
            r = requests.get(f"https://{url}")
            key = url.split('.')[0]

            soup = BeautifulSoup(r.content, 'html.parser')
            with open(f"{dir_}/{key}", 'w') as f:
                for line in soup.find_all(tags):
                    if line.name == 'a':
                        print(Fore.BLUE + line.get_text())
                        f.write(Fore.BLUE + line.get_text())
                    else:
                        print(line.get_text())
                        f.write(line.get_text())
