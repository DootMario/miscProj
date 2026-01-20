import csv

lista=[]
csvfile=open('catalog.csv','r')
reader=csv.reader(csvfile)

header=next(reader)
header.append('avg')

lista.append(header)

for row in reader:
    row.append(str((int(row[2])+int(row[3]))/2))
    lista.append(row)

csvfile.close()

csvout=open('catalog.csv','w')
writer=csv.writer(csvout)
writer.writerows(lista)

csvout.close()