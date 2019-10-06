import sys
_ = input()
lines = [line.strip('\n') for line in sys.stdin]
ins = [lines[i] for i in range(len(lines)) if i % 2 == 1]
def fixer(s):
    s = s.split(' ')
    if s[-1] == '': s.pop()
    return list(map(int,s))
ins = list(map(fixer,ins))
import functools
def f2(li):
    dp = li[:]
    for i in range(1, len(li)):
        for j in range(i):
            if li[j] < li[i]:
                dp[i] = max(dp[i], dp[j] + li[i])
    return max(dp)
def f1(li):
    @functools.lru_cache()
    def f(i):
        nonlocal li
        if i == 0: return li[i] 
        m = li[i]
        for j in range(0,i):
            if li[j] < li[i]:
                m = max(f(j) + li[i], m)
        return m
    answer = []
    for i in range(len(li)):
        answer.append(f(i))
    return max(answer)

ans = list(map(f1,ins))

for a in ans:
    print(a)