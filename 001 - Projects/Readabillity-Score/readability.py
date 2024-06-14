# Write your code here
import math
import re
import sys
import nltk
nltk.download('punkt')

with open(sys.argv[1], 'r') as file:
    text = file.readline()
    sentences = nltk.sent_tokenize(text)

vowels, hidden, words = [], [], []
for line in sentences:
    words.extend(nltk.regexp_tokenize(line, "[0-9A-z']+"))
    vowels.extend(re.findall(r'[aeiouyAEIOUY]+', line))
    hidden.extend(re.findall(r'[eE][ \.]', line))

characters = sum([len(line.replace(" ", '')) for line in sentences])
syllable = 0
for sy in vowels:
    syllable += 1 if len(sy) < 3 else 2

with open(sys.argv[2], 'r') as file:
    common_words = [line.rstrip() for line in file]
hard_words = []
for word in words:
    if word not in common_words:
        hard_words.append(word)

hard_words = len(hard_words)
syllable -= len(hidden)
words = len(words)
sentences = len(sentences)

print("Text:", text, '\n')
print("Characters:", characters)
print("Sentences:", sentences)
print("Words:", words)
print("Difficult words:", hard_words)
print("Syllables:", syllable, '\n')

avg_age = 0
index = math.ceil(4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43)
age = index + 4
age2 = age + 4 if age == 18 else age + 1
print("Automated Readability Index:", f"{index}. The text can be understood by {age}-{age2} year olds.")
avg_age += age + age2

index = math.ceil(0.39 * (words / sentences) + 11.7 * (syllable / words) - 15.59)
age = index + 4
age2 = age + 4 if age == 18 else age + 1
print("Flesch–Kincaid Readability Test:", f"{index}. The text can be understood by {age}-{age2} year olds.")
avg_age += age + age2

hard_words_percent = (hard_words / len(common_words)) * 100
index = 0.1579 * (hard_words / words) * 100 + 0.0496 * (words / sentences)
if hard_words_percent > 5:
    index = math.ceil(index + 3.6365)
else:
    index = math.ceil(index)
age = index + 4
age2 = age + 4 if age == 18 else age + 1
print("Dale-Chall Readability Index:", f"{index}. The text can be understood by {age}-{age2} year olds.")
avg_age += age + age2

print(f"This text should be understood in average by {avg_age / 6} year olds.")
