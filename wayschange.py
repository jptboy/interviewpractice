from typing import List
'''
Recursive relation
'''
def f(amount, coins):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif len(coins) == 0:
        return 0
    return f(amount - coins[-1], coins) + f(amount, coins[:-1])
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # make dp array
        # m x n
        # m = 0 to amount
        # n = [] to coins[:]
        dp = [[0]*(len(coins) + 1) for _ in range(amount + 1)]
        for i in range(amount + 1):
            for j in range(len(coins) + 1):
                if i == 0:
                    # if first row, ways to make change for amount 0 with any denoms is
                    # 1
                    dp[i][j] = 1
                elif j == 0:
                    # if first col and i != 0, you can't make change for any amount more than
                    # 0 with no coins so set to 0
                    dp[i][j] = 0
                else:
                    # see what new value would be if you used coin
                    coin = coins[j-1]
                    checkcoin = i - coin
                    if checkcoin >= 0:
                        # relation is #(ways to make change for new amount if you used coin) + #(ways to make change for amount if you didn't use coin)
                        v1 = dp[checkcoin][j]
                    else:
                        # if new coin is negative you can't make change for new amount, so this half of the ways to make change is 0
                        # eg making change for 4 dollars with only 5 dollar coin available
                        v1 = 0
                    # v2 is make change for same amount without using current coin, go back one col in matrix
                    v2 = dp[i][j - 1]
                    # relation is v1 + v2
                    dp[i][j] = v1 + v2 
        # return rightmost diagonal in dp array, make change for amount with all coins
        return dp[-1][-1]
s = Solution()
ans = s.change(5,[1,2,5])
x = 2