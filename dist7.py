#setup

og = []
n=int(input("Length?: "))
for _ in range(n):
    og.append(int(input("Element?: ")))

#sort this, the python implementation of the .sort() method is timsort, which to my understanding is a combination between merge and insertion sort,
#and its also stable(meaning the relative position of same value elements remains the same after manipulation). also sorting it in reverse cus that's easier to work with

og.sort(reverse=True)

#iniatate empty arrays to build solutions, as well as sums to keep track of the amount of value allocated to either partition

first = []
second = []
#put the first largest value in a distribution
s1=og[0]
first.append(og[0])
s2=0

#start a counter for elements left
k=1

#iterate through the elements of the og list and put them into either of the lists depending on which one is behind in
#value, it won't always reach the optimal solution(?) there are certainly edge cases that have a solution where the delta
#between partition values is smaller but I cant think of another solution that could counter that besides just backtracking
#all of them and picking the best one so yeah, id like to trade some ideal distribution for not having to generate some 100 solutions
#for a sub double-digit vector

while True:
    if k==n-1:
        break
    if s1>s2+og[k]:
        s2=s2+og[k]
        second.append(og[k])
    else:
        s1=s1+og[k]
        first.append(og[k])
    k=k+1

#show the solution we reached

print(first)
print(second)












