fin = open("dataset.txt","r")
nums=[int(_) for _ in fin.readline().split()]
fin.close()
for i in nums:
    if i%2==0:
        print(i,end=" ")
