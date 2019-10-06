from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1: return False
        nums.sort()
        half = int(s/2)
        dp = [[0]*(len(nums)+1) for _ in range(half + 1)]
        for i in range(half+1):
            used = set()
            for j in range(len(nums)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    weight = nums[j-1]
                    temp = i - weight
                    if temp < 0:
                        v1 = 0
                    else:
                        v1 = weight + dp[temp][j]
                    v2 = dp[i][j-1]
                    if v2 >= v1:
                        used.add(nums[j-2])
                    elif v1 > v2:
                        used.add(nums[j-1])

        if dp[-1][-1] != half:
            return True
        else:
            return False
s = Solution()
ans = s.canPartition([1,2,5])
x = 2
import functools
class SolutionWorking:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        half = int(s/2)
        @functools.lru_cache()
        def f(sumer, i):
            if sumer == half: return True
            if sumer > half or i >= len(nums): return False
            return f(sumer + nums[i], i + 1) or f(sumer, i + 1)
        return f(0,0)