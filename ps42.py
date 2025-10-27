n=int(input())

s=0

for i in range(n):
    s=s+int(input())

print(f"{n*(n+1)//2-s} is missing")

#runs on O(n) time cus we just subtract the actual sum from the supposed sum if there were all 1 through n numbers