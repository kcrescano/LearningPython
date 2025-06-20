import xml.etree.ElementTree as tree

root = tree.fromstring(input())
for element in root:
    print(element.text)
