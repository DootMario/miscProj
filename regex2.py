import re


sen = input()

pattern = re.compile('[0-9]{3,}')
print(pattern.findall(sen))