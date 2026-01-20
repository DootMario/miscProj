f=open("cadouri.txt","r")
t=f.readlines()
d={}
for i in t:
    x=i.split(",")
    if x[0] in d:
        d[x[0]]+=1
    else:
        d[x[0]]=1

f.close()
f1=open("raport.txt",'w')
for e in d:
    f1.write(f"{e}:{d[e]}\n")
f1.close()
