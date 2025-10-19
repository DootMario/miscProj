#a
#cautare binara
#operatie dom = x==(a[start]+a[end])//2
#nr op = log2(n)
def check(a, x):
    start=0
    end=len(a)-1
    while start<end:
        if x==(a[start]+a[end])//2:
            return True
        elif x<(a[start]+a[end])//2:
            end=(a[start]+a[end])//2-1
        elif x>(a[start]+a[end])//2:
            start=(a[start]+a[end])//2+1
    return False

#b
#sortare prin interclasare cu specificatia ca daca a[i]=b[j] luam unul si trecem mai departe in ambii vectori
#operatie dom = ab.append(a[i])
#nr op = m ?
def reunite(a, b):
    i=0
    j=0
    ab=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            ab.append(a[i])
            i=i+1
        if a[i]>b[j]:
            ab.append(b[j])
            j=j+1
        elif a[i]==b[j]:
            ab.append(a[i])
            i=i+1
            j=j+1

    if i<len(a):
        for i in range(i, len(a)):
            ab.append(a[i])
    if j<len(b):
        for j in range(j, len(b)):
            ab.append(b[j])

    return ab

#c
#parcurg prima multime si adaug in intersectie doar elementele din ea care apar si in a doua multime
#op dom = a[i] in b
#nr op = m
def intersect(a, b):
    ab=[]
    for i in range(len(a)):
        if a[i] in b:
            ab.append(a[i])

    return ab

#d
#parcurg a si daca elementul din a nu se gaseste in b il adaug in diferenta
#op dom = a[i] not in b
#nr op = m
def diff(a, b):
    ab=[]
    for i in range(len(a)):
        if a[i] not in b:
            ab.append(a[i])
    return ab

