#take the word and make a what's it called? attendance vector for the letters in it, simple function and then compare that
#with the same thing of all the words in the dictionary


#alternatively you could just iteratively filter for every letter in all words and cut them out of the dictionary as you do
#for example search for the letter a and

#wait much better idea, search for the letters of the word in every word in the dict, when u find it ofc. remove it
#eventually all the words that are anagrams will be left blank, empty strings, and then you just iterate through the dict
#counting them, weird af implementation, but I mean, it's good? maybe?

f=open("top_english_words_mixed_50000.txt", "r")

dex=f.readlines()

word=input("enter word:")
anagram=[]

for l in word:
    for w in dex:
        if l in w:
            dex[dex.index(w)]=w.replace(l,'*', 1)

last=0
for w in dex:
    if w.strip() == "*"*len(word):
        anagram.append(dex.index(w,last))
        last=dex.index(w,last)

f.seek(0,0)

for i, line in enumerate(f):
    if i in anagram:
        print(line, end='')

f.close()
