import re


sentence = input()

pattern = re.compile('07[0-9]{8}')
print(pattern.findall(sentence))