

import functools
inputs = [8,7]
def f(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        if i % 2 == 0:
            dp[i] = 1 + dp[int(i/2)]
        elif i%2 == 1:
            dp[i] = 2 + dp[int((i-1)/2)]
    return dp[-1]

def recursive(n):
    if n <= 1: return n
    if n % 2: return 2 + recursive(int((n-1)/2))
    return 1 + recursive(int(n/2))
answer = list(map(recursive,inputs))
for a in answer:
    print(a)
