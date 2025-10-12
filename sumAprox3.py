import math


phi = 0.01
n=int(input())
x=int(input())
s=0
count=0
for i in range(n+1):
    s=s + ((-1 ** i) * ((x ** (2 * i + 2)) / math.factorial(2*i+2)))
    count=i

print(s)
sn=s + ((-1 ** (count+1)) * ((x ** (2 * (count+1) + 2)) / math.factorial(2*(count+1)+2)))
count=count+2
while sn-s>phi:
    s=sn
    sn=sn+((-1 ** count) * ((x ** (2 * count + 2)) / math.factorial(2*count+2)))
    count=count+1

print(sn)