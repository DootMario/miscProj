sen1=input()
sen2=input()

sen1=sen1.lower()
sen2=sen2.lower()

dick1={}
dick2={}

for i in sen1:
    if i.isalpha():
        if i in dick1.keys():
            dick1[i]+=1
        else:
            dick1.update({i:1})

for i in sen2:
    if i.isalpha():
        if i in dick2.keys():
            dick2[i]+=1
        else:
            dick2.update({i:1})


ok=1
for i in dick1.keys():
    if i not in dick2.keys() or dick1[i]!=dick2[i]:
        print("False")
        ok=0
        break

if ok:
    print("True")
