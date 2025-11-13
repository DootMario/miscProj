def gen_fibo(n):
    x=1
    y=1
    yield x
    for i in range(1,n):
        yield y
        aux = y
        y = x+y
        x = aux
