l=[]
with open("copii.txt",'r') as f:
    t=f.readlines()
    for i in t:
        x=i.split(" ")
        l.append(x)

l.sort(key=lambda x:x[1],reverse=True)

with open("cumintei.txt",'w') as f:
    for i in l:
        if int(i[1])>=10:
            f.write(f"{i[0]}:{i[1]}\n")

