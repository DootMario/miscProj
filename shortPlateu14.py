n=int(input("enter the number: "))

newN=0
last=-1
cur=0
p=0
while n:
    cur=n%10
    if cur!=last:
        newN=newN+cur*(10**p)
        p=p+1
    last=cur
    n=n//10

print(newN)
