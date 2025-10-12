def fib(n):
    if n<=2:
        return 1

    else:
        return fib(n-1)+fib(n-2)

n=int(input("cate fib?:"))

for i in range(1,n+1):
    print(fib(i))