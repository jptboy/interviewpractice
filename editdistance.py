import functools
@functools.lru_cache()
def editDist(w1, w2):
    if w1 == w2: return 0
    if w1 == "": return len(w2)
    if w2 == "": return len(w1)
    return min(
        1 + editDist(w1[:-1], w2), # deletion delete last character of w1 1 op + editdistance of w1 without last char and w2
        # d o
        # d o g
        # insert g 1 op
        # d o g
        # d o g
        # then just check the rest of the string, so we are back to o in the first string, and we
        # move to i in the second string
        1 + editDist(w1,w2[:-1]), # insert w2[-1] to the end of w1, next call would be 
        # editDist(w1+w2[-1], w2) and since w1[-1] would be w2[-1] it would just do editDist(w1[:-1], w2[:-1])
        # where w1[:-1] would just be the w1 at the start, but we would be the w2[:-1] for the original w2
        editDist(w1[:-1], w2[:-1]) if w1[-1] == w2[-1] else 1 + editDist(w1[:-1], w2[:-1])
        # if the last character is the same just check the rest of the string
        # otherwise replace the last char which is 1 op and do the rest of the string
    )
ans = editDist("thequickbrownfoxjumpedoverthelazydog", "lazycatsareworsethanlazydogs")
def editDistDp(w1, w2):
    if w1 == w2: return 0
    if w1 == "": return len(w2)
    if w2 == "": return len(w1)
    dp = [[0]*(len(w2) + 1) for _ in range(len(w1) + 1)]
    for i in range(len(w1) + 1):
        for j in range(len(w2) + 1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            else:
                insert = 1 + dp[i][j-1] # j is index of w2, go back on w2
                delete = 1 + dp[i - 1][j] # i is index of w1, go back on w1
                # rest of str is diagonal up to left
                replace = dp[i - 1][j - 1] if w1[i - 1] == w2[j - 1] else 1 + dp[i - 1][j - 1]
                dp[i][j] = min(insert,delete,replace)
    return dp[-1][-1]

ans = editDistDp("a", "b")
x = 2