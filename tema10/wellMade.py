parenthesis= "([]{})"

depth = 0

depths=[]

for i in range(len(parenthesis)):
    if parenthesis[i] in "([{":
        depth += 1
        depths.append([depth, i])
    if parenthesis[i] in ")}]":
        depths.append([depth, i])
        depth -= 1

depths.sort(key=lambda x: x[0])
print(depths)
i=0
ok=1
depths.append([-1, 67])
while i < len(depths)-1:
    k=0
    while depths[i][0] == depths[i+1][0]:
        k=k+1
        i=i+1
    if (k+1)%2:
        print("nu e bine")
        ok=0
        break
    for j in range(i-k,i+1,2):
        if not ((parenthesis[depths[j][1]]=="(" and parenthesis[depths[j+1][1]]==")") or (parenthesis[depths[j][1]]=="[" and parenthesis[depths[j+1][1]]=="]") or (parenthesis[depths[j][1]]=="{" and parenthesis[depths[j+1][1]]=="}")):
            print("nu e bine")
            ok=0
            break
    if ok==0:
        break
    i=i+1

print(depths)
if ok:
    print("e bine")
