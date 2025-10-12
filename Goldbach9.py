import math
import time

primes=[]

def prime(x):
    if x in primes:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(x))):
            if x % i==0:
                return False
        primes.append(x)
        return True


def gold(x):
    for i in range(2, x-1):
        if prime(i) and prime(x-i):
            return True

    return False


x=4
start = time.time()
dur=int(input("How long? (minutes): "))*60
while True:
    if not gold(x) or time.time()-start >= dur:
        print(f"Finished at {x} valued at {gold(x)} in {time.time()-start/60} minutes.")
        break
    x+=2
