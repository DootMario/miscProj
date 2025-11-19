def identic5(x):
    i=-1
    while i<len(x):
        i=i+1
        if x[i-1]!=x[i]:
            return False
    return True

x1 = [2,2,2,2,2,2]
x2 = [2,2,2,2,3]
x3 = [2,2,3,3,2,2]

print(identic5(x1))
print(identic5(x2))
print(identic5(x3))