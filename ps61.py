import dataSet


n = int(input())

a = [random.randint(1,n) for _ in range(n)]

print(a)

for i in range(n-1, -1, -1):
    if a[i] > a[i-1]:
        a[i]=a[i]+a[i-1]
        a[i-1]=a[i]-a[i-1]
        a[i]=a[i]-a[i-1]

print(a)