import sys
sys.setrecursionlimit(10000)
import functools
def rodcut(tup):
    rodlengt, cutlengths = tup
    cutlengths = list(set(cutlengths))
    if rodlengt < min(cutlengths):
        return 0
    mincutl = min(cutlengths)
    @functools.lru_cache()
    def f(rodlength):
        nonlocal mincutl
        # if rodlength < minimum cutlengths return 0 which is invalid
        if rodlength < mincutl: return 0
        # set curmax to 0, the whole operation on the rod could be invalid
        # so we set to 0
        curmax = 0
        for cutlength in cutlengths:
            if rodlength >= cutlength:
                if rodlength == cutlength:
                    curmax = max(1, curmax)
                else:
                    ret =  f(rodlength - cutlength)
                    if ret == 0:
                        curmax = max(curmax, 0)
                    else:
                        curmax = max(1 + ret, curmax)
        return curmax
    return f(rodlengt)

def rodcutdp(tup):
    rodlength, cutlengths = tup
    cutlengths = sorted(list(set(cutlengths)))
    mincutl = min(cutlengths)
    if rodlength < mincutl: return 0
    dp = [[0]*(len(cutlengths) + 1) for _ in range(rodlength + 1)]
    for i in range(1, (rodlength + 1)):
        for j in range(1, len(cutlengths) + 1):
            if i < mincutl:
                # if rodlength < mincut length set to invalid
                dp[i][j] = 0
            else:
                # check what nextrodlength would be if we make cut
                nextrodlength = i - cutlengths[j - 1]
                if nextrodlength == 0:
                    # if nextrodlength would be zero then v1 is 1
                    # because we will have 1 piece
                    v1 = 1
                elif nextrodlength < 0:
                    # if it would be negative, then v1 is obv invalid
                    v1 = 0
                else:
                    # if it does have a length more than 0
                    # check if that newrodlength with the first j cutlengths is valid or not
                    v1 = dp[nextrodlength][j]
                    if v1 == 0:
                        v1 = 0
                    else:
                        # if its valid we have dp[nextrodlength][j] + 1 pieces
                        v1 = v1 + 1
                # check max pieces if we don't use this cutlength
                v2 = dp[i][j - 1]
                dp[i][j] = max(v1, v2)
    return dp[-1][-1]
ans = rodcutdp((5, [5,3,2]))
ans2 = rodcutdp((4,[2,1,1]))
ans3 = rodcutdp((4000,[1,2,3]))
ans4 = rodcutdp((3,[1,2]))
ans5 = rodcutdp((7,[5,5,2]))
ansr = rodcut((5, [5,3,2]))
ans2r = rodcut((4,[2,1,1]))
ans3r = rodcut((4000,[1,2,3]))
ans4r = rodcut((3,[1,2]))
ans5r = rodcut((7,[5,5,2]))
x = 2