import os
#library for interfacing with the os


quer=input("Search by what?: (yYYYYmMMdDD) ")
qyear=""
qmonth=""
qday=""

if "y" in quer:
    qyear=quer[quer.index("y")+1:quer.index("y")+5:]
if "m" in quer:
   qmonth=quer[quer.index("m")+1:quer.index("m")+3:]
if "d" in quer:
    qday=quer[quer.index("d")+1:quer.index("d")+3:]


for filename in os.listdir("./logs"):
    if qyear in filename[:4:] and qmonth in filename[4:6:] and qday in filename[6::]:
        print("Found log file: " + filename)
