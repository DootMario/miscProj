import random


n = int(input())
k = int(input())

vec = [random.randint(1,n) for _ in range(n)]

vec.sort()

print(vec)

i=1
j=1

while i<n and j<k:
    if vec[i]!=vec[j-1]:
        vec[j]=vec[i]
        j=j+1

    i=i+1

print(vec[:6:])

#ordin de complexitate O(n,k)