import json
d={}
with open('dorinte.json','r')as f:
    data=json.load(f)
    for dictionar in data:
        for elem in dictionar['listadorinte']:
            if elem[0] not in d:
                d[elem[0]]=1/elem[1]
            else:
                d[elem[0]]+=1/elem[1]
print(max(d,key=lambda x:d[x]))

