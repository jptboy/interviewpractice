import sys
x = [line.strip('\n').rstrip() for line in sys.stdin]
cases = int(x[0])

del x[0]

inputs = []
for i in range(cases):
    itr = 3 * i
    inputs.append((x[itr + 1], x[itr + 2]))

def f(tup):
    first, second = tup
    if first in second or second in first:
        return min(len(first),len(second))
    dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    m = 0
    for i in range(1,len(first) + 1):
        for j in range(1,len(second) + 1):
            letter2 = second[j-1]
            letter1 = first[i-1]
            if letter2 == letter1:
                if i - 1 > 0 and j - 1 > 0:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1
                m = max(dp[i][j],m)
    return m
answer = list(map(f, inputs))
for ans in answer:
    print(ans)