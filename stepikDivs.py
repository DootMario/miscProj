n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

divs = {}

for i in numbers:
    divi = []
    for j in range(2, i//2+1):
        if i % j == 0:
            divi.append(j)

    if divi:
        divs.update({i:divi})

for i in divs:
    print(f"{i}: {divs[i]}")
