import random

n=int(input())
m=int(input())

mat = [[random.randint(n,m+n) for _ in range(n)] for _ in range(m)]

x = int(input())

for i in range(n):
    for j in range(m):
        if mat[i][j] == x:
            print(f"{x}: {mat[i][j]}")
            quit()


print(f"{x}: not found")

#0(n,m)