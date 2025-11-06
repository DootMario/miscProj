N = int(input())

frequency={}

for i in range(N):
    line=input()
    words=line.split()
    for w in words:
        if w in frequency:
            frequency[w]+=1
        else:
            frequency.update({w:1})

for i in frequency.keys():
    if frequency[i]>1:
        print(f"{i} {frequency[i]}")