class Knap:
    def __init__(self, items, weight, values, weights):
        self.weight = int(weight)
        self.items = int(items)
        temp1 = values.split(' ')
        temp1.pop()
        temp2 = weights.split(' ')
        temp2.pop()
        self.values = list(map(int,temp1))
        self.weights = list(map(int,temp2))

def f(self):
    N, W, values, weights = self.items, self.weight, self.values, self.weights
    good = list(zip(values, weights))
    good.sort(key = lambda x: x[1])
    dp = [[0]*(W + 1) for _ in range(len(good) + 1)]
    for i in range(1,len(good) + 1):
        for j in range(1, W + 1):
            newW = j - good[i - 1][1]
            if newW < 0:
                v1 = float('-inf')
            else:
                # i - 1 newV because we want to add the max value without using the ith item, at thew new weight. 
                # we cant stay on the same row because we used the item so we do i - 1
                v1 = dp[i-1][newW] + good[i - 1][0]
            # not using the item so we keep the weight
            v2 = dp[i - 1][j]
            dp[i][j] = max(v1, v2)
    return dp[-1][-1]
def recursive(self):
    N, W, values, weights = self.items, self.weight, self.values, self.weights
    good = list(zip(values, weights))
    good.sort(key = lambda x: x[1])
    def f1(i, W):
        if W <= 0 or i < 0: return 0
        if W - good[i][1] < 0: return f1(i - 1, W)
        return max(f1(i - 1, W), good[i][0] + f1(i - 1, W - good[i][1]))
    return f1(len(good) - 1, W)
# no items, max cap, values, weights
ans = f(Knap("3","4","1 2 3 ", "4 5 1 "))
ans2 = recursive(Knap("3","4","1 2 3 ", "4 5 1 "))
x = 2