def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def power(x, n):
    if n==1:
        return x
    if n==2:
        return x*x
    else:
        return x*power(x,n-1)

def fin_sum(x, n):
    s=0.0
    for i in range(1,n+1):
        s=s+((power(-1, i)*power(x,2*i))/factorial(2*i))
        s = s + (((-1 ** i) * (x ** (2 * i))) / factorial(2 * i))
    return s

