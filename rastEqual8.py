import math

n=int(input())
s1=[0]*n
s2=[0]*n

def flip(pan, farfurie):
    for i in range(math.ceil(pan/2)):
        aux = farfurie[i]
        farfurie[i] = farfurie[pan-i]
        farfurie[pan-i] = aux

for i in range(n):
    s1[i]=int(input())

for i in range(n):
    s2[i]=int(input())

for i in range(1,n+1):
    flip(i, s1)
    if s1==s2:
        break
    else:
        flip(i, s1)

if s1==s2:
    print("YES")
else:
    print("NO")
