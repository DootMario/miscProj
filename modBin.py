rot = [0, 1, 2, 3, 4, 5, 6, 7]

for j in range(4):
    aux = rot[7]
    for i in range(7, 0, -1):
        rot[i] = rot[i-1]
    rot[0]=aux
print(rot)

shift=rot[0]

low=shift
high=(low-1)%len(rot)

x=int(input("Mi-l dai?: "))

while (low-shift)%len(rot)<=(high-shift)%len(rot):
    mid=(low+high)//2%len(rot)
    if x==rot[mid]:
        print(x)
        break
    if x<rot[mid]:
        high=(mid-1)%len(rot)
    else:
        low=(mid+1)%len(rot)