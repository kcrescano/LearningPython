# mine
from collections import Counter
print(Counter(input().split()).most_common(1)[0][0])
# Hyperskill user posted solution
lst = input().split()
print(max(lst, key=lst.count))
