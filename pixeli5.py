import dataSet


class Pixel:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
        #subpunct a
        self.value = (max(r,g,b)+min(r,g,b))/2

n = int(input("enter img resolution: "))

screen = [[Pixel(random.randint(0,256),random.randint(0,256),random.randint(0,256)) for i in range(n)]for j in range(n)]

#b
hist=[0]*256

for i in range(n):
    for j in range(n):
        hist[screen[i][j].value]+=1

#c
s = 0
d = 0
for i in range(256):
    s = s+hist[i]*i
    d = d+hist[i]

avg = s/d

#d
for i in range(n):
    for j in range(n):
        if screen[i][j].value>=avg:
            screen[i][j].value=1
        else:
            screen[i][j].value=0

#e
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            if screen[i][j].value==0:
                print("False")
                quit()
        else:
            if screen[i][j].value==1:
                print("False")
                quit()
