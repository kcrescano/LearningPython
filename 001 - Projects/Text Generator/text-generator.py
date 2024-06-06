# Write your code here
import nltk
import random


with open(f"{input()}", encoding="utf-8") as file:
    textfile = file.read()
    token = nltk.WhitespaceTokenizer().tokenize(textfile)
    trigram = list(nltk.trigrams(token))

markov = {}
for h, h2, t in trigram:
    markov.setdefault((h, h2), {})
    markov[(h, h2)][t] = markov[(h, h2)].get(t, 0) + 1

for i in range(10):
    while (not (head := random.choice(list(markov.keys())))[0][0].isupper()
           or head[1][-1] in '.!?'
           or head[0][-1] in '.!?'):
        ...

    sen = [*head]
    head = (head[1], random.choice(list(markov[head])))

    while len(sen) < 4 or head[1][-1] not in '.!?':
        sen.append(head[1])
        head = (head[1], random.choice(list(markov[head])))

    sen.append(head[1])
    print(" ".join(sen))
