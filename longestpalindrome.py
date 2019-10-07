import functools
def f(s):
    @functools.lru_cache()
    def f1(i):
        nonlocal s
        if i == 0: return s[i]
        m = s[i]
        for j in range(i):
            otherS = s[j:i+1]
            if otherS == "".join(reversed(otherS)) and len(otherS) > len(m): m = otherS
        return m
    ret = [f1(i) for i in range(len(s))]
    m = ""
    for r in ret:
        if len(r) >  len(m): m = r
    return m
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        revs = "".join(reversed(s))
        if s == revs: return s
        dp = [[0]*len(s) for j in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == revs[j]:
                    dp[i][j] = 1
        m = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == 1:
                    tempS = []
                    tempi, tempj = i,j
                    cnt = 0
                    while tempi < len(s) and tempj < len(s) and dp[tempi][tempj] == 1:
                        tempS.append(s[tempi])
                        dp[tempi][tempj] = 0
                        cnt += 1
                        tempi += 1
                        tempj += 1
                    if tempS[::-1] == tempS:
                        if len(tempS) > len(m): m = "".join(tempS)
        return m
ans = f("babadada")
ans2 = Solution().longestPalindrome("babadada")
x = 2