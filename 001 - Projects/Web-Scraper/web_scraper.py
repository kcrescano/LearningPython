import requests
from bs4 import BeautifulSoup
import string, os


page_n, article_type = int(input()), input()

for page in range(page_n):
    try:
        os.mkdir(f"Page_{page + 1}")
    except FileExistsError:
        pass

    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page+1}"
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')

    if response.status_code == 200:
        for article in soup.findAll("article"):
            if article.find("span", {"class": "c-meta__type"}).text.lower() == article_type.lower():
                filename = article.find("h3", {"class": "c-card__title"}).text
                for char in string.punctuation:
                    filename = filename.replace(char, "")
                filename = filename.replace("\n", "")
                filename = filename.replace(" ", "_")

                url = "https://www.nature.com" + article.find("a").get("href")
                response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
                soup = BeautifulSoup(response.content, 'html.parser')

                file = open(f"Page_{page + 1}/{filename}.txt", "wb")
                file.write(soup.find("p", {"class": "article__teaser"}).text.encode())
                file.close()
    else:
        print("The URL returned", response.status_code)
