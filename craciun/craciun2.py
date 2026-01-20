import csv
d={}
s=set()
s2=set()
with open("spiridusi.csv",'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    sum=0
    for row in reader:
        if row[0] not in s2:
            s2.add(row[0])
        if int(row[1])>8 and row[0] not in s:
            s.add(row[0])
            print(row[0])
        sum=sum+int(row[1])

    m=sum/len(s2)
    print(round(m,1))

for e in s:
    print(e)
