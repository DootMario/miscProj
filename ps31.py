import dataSet


n=int(input("enter n: "))
m=int(input("enter m: "))
mat=[[random.randint(0,1) for i in range(n)] for j in range(m)]

l=0
length=0

longest=[0]*3

for i in range(n):
    length=0
    for j in range(m):
        if mat[i][j]==1 and (mat[i-1][j]==0 or i-1<0) and (mat[i+1][j]==0 or i+1>n-1):
            length+=1
        if (mat[i][j]==0 or j==m-1) and length>=2:
            if length > longest[2]-longest[1]+1:
                longest[2]=j-1
                longest[1]=j-1-length
                longest[0]=i
            l=l+1
            length=0

print(l)
print(f"line:{longest[0]}, columns:{longest[1]} to {longest[2]}")
