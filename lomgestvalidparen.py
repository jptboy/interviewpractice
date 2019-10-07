def f(s):
    if len(s) <= 1: return 0
    if len(s) == 2: return 2 if s == "()" else 0
    stack = []
    didremove = [0] * len(s)
    dp = didremove[:]
    for tup in enumerate(list(s)):
        stack.append(tup)
        index, i = tup
        if i == ')' and len(stack) > 1 and stack[-2][1] == "(":
            stack.pop()
            indexremoved, _ = stack.pop()
            numberOfParens = (2 + ((index - indexremoved) - 1))
            didremove[index] = (indexremoved, numberOfParens)
    if didremove[1] != 0:
        dp[1] = 2
    for i in range(2, len(s)):
        if didremove[i] != 0:
            indexdestroyed, numparens = didremove[i]
            dp[i] = numparens
            if indexdestroyed > 0 and dp[indexdestroyed - 1] != 0:
                dp[i] += dp[indexdestroyed - 1]
            
    return max(dp)
def f2(s):
    if len(s) <= 1: return 0
    if len(s) == 2: return 2 if s == "()" else 0
    stack = []
    dp = [0]*len(s)
    parensArr = dp[:]
    for i in range(len(s)):
        char = s[i]
        tup = i, char
        stack.append(tup)
        numberOfParens = 0
        if char == ")" and len(stack) > 1 and stack[-2][1] == '(':
            stack.pop()
            indexremoved, _ = stack.pop()
            numberOfParens = 2 + ((i - indexremoved) - 1)
            if indexremoved > 0:
                numberOfParens += parensArr[indexremoved - 1]
            parensArr[i] = numberOfParens
        dp[i] = max(numberOfParens, dp[i-1])
    return dp[-1]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0: return 0
        stack = []
        dp = [0]*len(s)
        parensArr = dp[:]
        for i in range(len(s)):
            char = s[i]
            tup = i, char
            stack.append(tup)
            numberOfParens = 0
            if char == ")" and len(stack) > 1 and stack[-2][1] == '(':
                stack.pop()
                indexremoved, _ = stack.pop()
                numberOfParens = 2 + ((i - indexremoved) - 1)
                if indexremoved > 0:
                    numberOfParens += parensArr[indexremoved - 1]
                parensArr[i] = numberOfParens
            dp[i] = max(numberOfParens, dp[i-1])
        return dp[-1]
ans = f2("()()()")
x = 2