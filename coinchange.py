from typing import List
class Solution:
    def coinChange(self, D: List[int], v: int) -> int:
        m = {'0 ': 0}
        D = sorted(D)
        def handler(c1, c2):
            if c1 == float('inf') and c2 == float('inf'):
                return float('inf')
            else:
                return min(1+c1, c2)
        def hv(v,D):
            s = []
            s.append(str(v))
            s.append(' ')
            for c in D:
                s.append(str(c))
                s.append(' ')
            return "".join(s)
        def h(v,D):
            newD = [x for x in D if x <= v]
            return newD
        def f(v,D):
            hval = hv(v,D)
            if hval in m:
                return m[hval]
            elif len(D) == 0:
                return float('inf')
            elif v == 0:
                return float('inf')
            else:
                newV = v - D[-1]
                c1 = f(newV, h(newV, D))
                c2 = f(v,D[:-1])
                val = handler(c1,c2)
                m[val] = val
                return val
        ans = f(v,h(v,D))
        if ans == float('inf'):
            return -1
        else:
            return ans
sol = Solution()
def dp(v,D):
    D = sorted(D)
    arr = [[0] * (v+1) for _ in range(len(D) + 1)]
    arr[0][0] = 0
    for i in range(0,len(D) + 1):
        for j in range(1, v + 1):
            if i == 0:
                arr[i][j] = float('inf')
            else:
                v1 = arr[i-1][j]
                coinval = j - D[i-1]
                checkrow = None
                if coinval >= D[i-1]:
                    checkrow = i
                else:
                    checkrow = i - 1
                if coinval < 0:
                    v2 = float('inf')
                else:
                    v2 = arr[checkrow][coinval]
                arr[i][j] = min(v1, 1 + v2)
    ans = arr[-1][-1]
    if ans == float('inf'): return -1
    else: return ans

# print(sol.coinChange([1], 2))
print(dp(11,[2,11]))
