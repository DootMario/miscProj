#setup
#imports and setup to read the pancake stack that needs sorting

import math

farfurie = []

nr = int(input("Pankakes?: "))

for _ in range(nr):
    farfurie.append(int(input("Pankake size?: ")))

#flip function
#it just flips the part of the stack from the start to the element at the imputed index

def flip(pan):
    for i in range(math.ceil(pan/2)):
        aux = farfurie[i]
        farfurie[i] = farfurie[pan-i]
        farfurie[pan-i] = aux

# #final condition
#no longer needed since reccursively insert sorting it is faster (? i think ?)

# def check():
#     for i in range(nr-1):
#         if farfurie[i]>farfurie[i + 1]:
#             return False
#     return True

#actual sorting business
#it just insert sorts recursively presuming the top of the stack is sorted, which it initially is since any singular
#element is sorted by default and then just takes the next element in the stack and figures out where it needs to be
#inserted in the sorted section
#the insertion is preety simple you just take the unsorted element and take it to the top, then flip from just
#below the element thats larger than it then flip the stuff above it and finally flip the whole sorted section again
#so its right way up and u can call the function for the next element
#it stops when the recursive level is equal to the ammount of elements, since that means that (if the algorithm is correct)
#the stack is fully sorted

def sortStack(k=1):
    if k==nr:
        print(farfurie)
        return
    for i in range(k):
        if farfurie[i]>farfurie[k]:
            flip(k)
            flip(k-i)
            flip(k-i-1)
            flip(k)
            break
    sortStack(k+1)




#putting things in motion
sortStack()
