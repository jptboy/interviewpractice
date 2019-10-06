from typing import List
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)
        dp = [1]*len(arr)
        for i in range (1 , len(arr)): 
            for j in range(0 , i): 
                if arr[i] > arr[j]: dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
class Solution2:
    def lengthOfLIS(self, arr: List[int]) -> int:
        # if arr empty max length is 0
        if not arr: return 0
        import functools
        @functools.lru_cache()
        def f(i):
            nonlocal arr
            # max length at arr[0] is 1
            if i == 0: return 1
            # min length is 1
            m = 1
            for j in range(0,i):
                '''
                For all values of j that arr[i] could be appended to (if arr[j] < arr[i])
                arr[i] = the max of what arr[i] is or 1 + the max subseq length at arr[j]
                '''
                if arr[j] < arr[i]:
                    m = max(f(j) + 1,m)
            return m
        # calc max subseq length at every point in array and return max
        ans = [f(i) for i in range(len(arr))]
        return max(ans)

ans = Solution2().lengthOfLIS([10,9,2,5,3,7,101,18])
x = 2