a=int(input())
b=int(input())
r=0
while a:
    if a%21:
        r=r+b
    a=a//2
    b=b*2
print(r)