import csv


csvfile=open('catalog.csv','r')
reader=csv.reader(csvfile)
csvout=open('csvout.csv','w')
writer=csv.writer(csvout)

header=next(reader)
header.append('avg')

writer.writerow(header)

for row in reader:
    row.append(str((int(row[2])+int(row[3]))/2))
    writer.writerow(row)

csvfile.close()
csvout.close()