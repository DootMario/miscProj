rot = [0, 1, 2, 3, 4, 5, 6, 7]

for j in range(4):
    aux = rot[7]
    for i in range(7, 0, -1):
        rot[i] = rot[i-1]
    rot[0]=aux
print(rot)

shift=rot[0]

low=0
high=len(rot)-1

x=int(input("Mi-l dai?: "))

while low<=high:
    mid=(low+high)//2
    if x==rot[(mid+shift)%len(rot)]:
        print(x)
        break
    if x<rot[(mid+shift)%len(rot)]:
        high=mid-1
    else:
        low=mid+1