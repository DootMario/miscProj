n=int(input())
ap=[0]*10
while n>0:
    ap[n%10]=ap[n%10]+1
    n=n//10
big=0
for i in ap:
    if i>big:
        big=i
for i in ap:
    if i==big:
        print(ap.index(i))