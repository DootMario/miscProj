import random

from multimi4 import reunite,intersect

n=int(input("dati rez: "))

a=[[random.randint(0,1) for i in range(n)] for j in range(n)]
b=[[random.randint(0,1) for i in range(n)] for j in range(n)]

amult=[[]]
bmult=[[]]

for i in range(n):
    for j in range(n):
        amult[j*i+j].append(i)
        amult[j*i+j].append(j)
        amult[j*i+j].append(a[i][j])
        bmult[j*i+j].append(i)
        bmult[j*i+j].append(j)
        bmult[j*i+j].append(b[i][j])

reunite = reunite(amult, bmult)
intersect = intersect(amult, bmult)

print(len(intersect)/len(reunite))


