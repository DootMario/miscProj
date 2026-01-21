def subSeq(s, t):
    dp=[[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

    for i in range(len(dp[0])):
        dp[0][i] = 1

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            dp[i][j] = 1 if s[i-1] == t[j-1] and dp[i-1][j]==1 else dp[i][j-1]

    for i in dp:
        print(i)

    return dp[-1][-1]
    #
    #         nan a   z   c   d
    #     nan 1   1   1   1   1
    #     a   0   1   1   1   1
    #     b   0   0   0   0   0
    #     c   0   0   0   0   0


print(subSeq("abc","azbcd"))




