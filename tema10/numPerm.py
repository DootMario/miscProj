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
    if k==-1:
        for i in range(len(dig)-1):
            stack.clear()
            construct(available, k+1, stack, size+1)
    if k>=0:
        for i in range(len(available)):
            stack.append(available[i])
            nxt=available.pop(i)
            construct(nxt, k+1)
            stack.pop()

construct(dig)

