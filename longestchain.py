from typing import List
class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        k = lambda x: x[0]
        v = sorted(pairs, key = k)
        import functools
        @functools.lru_cache()
        def h(i):
            nonlocal v
            itr = i + 1
            while itr < len(v) and v[i][1] >= v[itr][0]:
                itr += 1
            return itr
        @functools.lru_cache()
        def f(i):
            nonlocal v
            if i >= len(v): return 0
            newi = h(i)
            return max(1 + f(newi), f(i + 1))
        return f(0)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        curpos = float('-inf')
        answer = 0
        pairs.sort(key = lambda x: x[1])
        for startpos,endpos in pairs:
            if curpos < startpos:
                curpos = endpos
                answer += 1
        return answer 
s = Solution()
arr = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
ans = s.findLongestChain(arr)
x = 2