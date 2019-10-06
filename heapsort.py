import math
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(i,a):
            if len(a) == 0: return
            leftIdx = 2*i + 1
            rightIdx = leftIdx + 1
            minv = a[i]
            swapIdx = -1
            if leftIdx < len(a):
                if a[leftIdx] < minv:
                    minv = a[leftIdx]
                    swapIdx = leftIdx
            if rightIdx < len(a):
                if a[rightIdx] < minv:
                    minv = a[rightIdx]
                    swapIdx = rightIdx
            if swapIdx != -1:
                a[i], a[swapIdx] = a[swapIdx], a[i]
                heapify(swapIdx,a)
        def heappop(a):
            a[0], a[-1] = a[-1], a[0]
            ret = a.pop()
            heapify(0,a)
            return ret
        def makeminheap(a):
            l = len(a)
            if l == 0 or l == 1:
                return
            else:
                index = int(2**math.floor(math.log(l,2)) - 2)
                for i in range(index,-1,-1):
                    heapify(i,a)
        makeminheap(nums)
        ans = []
        while len(nums) > 0:
            ans.append(heappop(nums))
        return ans

s = Solution()
print(s.sortArray([5,4,3,2,1]))