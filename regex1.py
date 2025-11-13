import re

sen=input()

words = sen.split()

for word in words:
    pattern = re.compile("[a-z]*[aeiou]{2}[a-z]*")

    if pattern.findall(word):
        print(word)
