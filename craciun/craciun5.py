import csv
d={}
with open("reni.csv",'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    max=-1
    for row in reader:
        if int(row[2])>max:
            max=int(row[2])
            renul=row[0]
        if row[0] in d:
            d[row[0]]=d[row[0]]+int(row[3])
        else:
            d[row[0]]=int(row[3])
    for ren in d:
        d[ren]=int(d[ren])/30

print(d)
print(renul)
