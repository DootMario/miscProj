n=int(input())
newN=0
k=int(input())
l=len(str(n))
i=0
while n:
    newN=newN+(n%10*(10**((i+k)%l)))
    n=n//10
    i=i+1

print(newN)
