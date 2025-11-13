import  re


sen=input()

pattern=re.compile(r'\w*\.?')
print(*[i for i in pattern.findall(sen) if i != ""],sep=' ')