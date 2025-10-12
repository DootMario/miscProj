a1,b1,a2,b2=input().split(" ")
a1=float(a1)
b1=float(b1)
a2=float(a2)
b2=float(b2)

if (a1 <= a2 <= b1) or (b1 >= b2 >= a1):
    print("YES")
else:
    print("NO")
