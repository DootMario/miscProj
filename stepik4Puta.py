sen = input()
lsen=list(sen)

for i in range(len(lsen)):
    if "a"<=lsen[i]<="z":
        lsen[i]=chr(ord(lsen[i])-32)

sen="".join(lsen)
print(sen)
