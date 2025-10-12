n=int(input())
one=0
while n>0:
    one=one+n%2
    n=n//2
print(one)