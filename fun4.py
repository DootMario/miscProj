def remove_duplicates(ln):
    i=0
    while i<len(ln)-1:
        j=i+1
        while j<len(ln):
            if ln[i]==ln[j]:
                ln.pop(j)
                j=j-1
            j=j+1
        i=i+1
ln = [8, 11, 12, 12, 12, 14, 15, 12]

remove_duplicates(ln)

print(ln)