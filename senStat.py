with open("dataset2.txt","r") as fin:
    dic={}
    for line in fin.readlines():
        for word in line.split():
            if word in dic:
                dic[word]+=1
            else:
                dic.update({word:1})

dic=dict(sorted(dic.items()))

for i in dic:
    print(i,dic[i])

