n=13324

dig=[]

while n:
    if n%10 not in dig:
        dig.append(n%10)
    n=n//10

dig.sort()

def construct(available, k=-1, stack=None, size=0):
    if stack is None:
        stack = []
    if k==size:
        print(stack)
        return 0
    if k==-1:
        for i in range(len(available)):
            stack.clear()
            size=size+1
            construct(available, k+1, stack, size)
    if k>=0:
        for i in range(len(available)):
            stack.append(available[i])
            nxt=[available[j] for j in range(len(available)) if j!=i]
            construct(nxt, k+1, stack, size)
            stack.pop()

construct(dig)

