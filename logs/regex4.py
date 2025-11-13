import re


sen = input()

pattern = re.compile(r'[a-z]+\.[a-z]+[00-99]*@e-uvt\.ro')
pattern2 = re.compile(r"[a-z]+\.[a-z]+@e-uvt\.ro")
print(pattern.findall(sen))