import numpy as np
def f(mat: np.ndarray,M,N):
    def dfs(i,j):
        nonlocal M
        nonlocal N
        nonlocal mat
        val = mat[i][j]
        if val == -1: return -1
        if i == M - 1 and j == N - 1: return 1
        mat[i][j] = -1
        ways = 0
        if i < M - 1:
            ret = dfs(i + 1, j)
            if ret != -1: ways += ret
        if j < N - 1:
            ret = dfs(i, j + 1)
            if ret != -1: ways += ret
        mat[i][j] = val
        return ways
    return dfs(0,0) % ((10**9) + 7)
def f2(mat: np.ndarray,M,N):
    memo = np.zeros((M,N))
    memo.fill(np.nan)
    def dfs(i,j):
        nonlocal M
        nonlocal N
        nonlocal mat
        nonlocal memo
        if not np.isnan(memo[i][j]): return memo[i][j]
        val = mat[i][j]
        if val == -1:
            memo[i][j] = -1
            return -1
        if i == M - 1 and j == N - 1:
            memo[i][j] = 1
            return 1
        ways = 0
        if i < M - 1:
            ret = dfs(i + 1, j)
            if ret != -1: ways += ret
        if j < N - 1:
            ret = dfs(i, j + 1)
            if ret != -1: ways += ret
        memo[i][j] = ways
        return ways
    return dfs(0,0) % ((10**9) + 7)
def f3(mat: np.ndarray,M,N):
    dp = np.zeros((M,N),dtype = int)
    for i in range(M - 1, -1, -1):
        for j in range(N - 1, -1 , -1):
            val = mat[i][j]
            if val == -1: dp[i][j] = -1
            elif i == M - 1 and j == N - 1: dp[i][j] = 1
            else:
                s = 0
                if i < M - 1 and dp[i + 1][j] != -1: s += dp[i + 1][j]
                if j < N - 1 and dp[i][j + 1] != -1: s += dp[i][j + 1]
                dp[i][j] = s if s != 0 else -1
    ret = int(dp[0][0])
    return 0 if ret == -1 else ret
tester = np.zeros((2,8))
tester[0][1] = -1
tester[0][6] = -1
tester[0][2] = -1
ans = f3(tester, 2, 8)
x = 2