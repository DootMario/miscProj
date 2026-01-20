def turnBack(og, l):
    back=[]
    for i in l:
        back.append(og[i])
    return back


def subSeq(s, t):
    dp=[[]for _ in range(len(s))]
    dp[0]=[[i] for i in range(len(t)) if s[0] == t[i]]

    '''
    dp = [0[[0],...], 1[[0,1],...], [[0,1,3]...]]
    
    '''

    for i in range(1,len(dp)):
        for j in dp[i-1]:
            for k in range(j[-1]+1,len(t)):
                new=j[::]
                if s[i] == t[k]:
                    new.append(k)
                dp[i].append(new)

    # for i in dp:
    #     print(i)

    for i in dp[-1]:
        if turnBack(t, i) == list(s):
            return True

    return False

print(subSeq("aaaaaa","bbaaaa"))




