kids={}

with open("cadouri.txt","r") as fin:
    group=[i.split(",")[0] for i in fin.readlines()]
    for i in group:
        if i not in kids:
            kids.update({i:1})
        else:
            kids[i]+=1

with open("raport.txt","w") as fout:
    for i in kids.keys():
        fout.write(f"{i},{kids[i]}\n")

