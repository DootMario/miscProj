
def hanoi(n, p1="s1", p2="s2", p3="s3"):
    if n==1:
        print(f"{p1}->{p3}")
    if n==2:
        print(f"{p1}->{p2}\n{p1}->{p3}\n{p2}->{p3}")
    else:
        hanoi(n-1, p1, p3, p2)
        print(f"{p1}->{p3}")
        hanoi(n-1, p2, p1, p3)


hanoi(4)
