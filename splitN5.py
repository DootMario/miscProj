n=int(input("numar?:"))
p=0
i=0
cp=1
ci=1
while n:
    if n%2==0:
        p=p+(n%10*cp)
        cp=cp*10
        n=n//10
    else:
        i=i+(n%10*ci)
        ci=ci*10
        n=n//10

print(p)
print(i)