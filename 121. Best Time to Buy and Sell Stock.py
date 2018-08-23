class Solution(object):
    def maxProfite(self, prices):
        n = len(prices)
        if n < 2:   # if only has buy in or no operation, no profit
            return None
        dp = [0]*n
        dp[0] = prices[0]
        res = 0
        for i in range(n):
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
            res = max(dp[i], res)
        return res



        # if len(prices) < 2:
        #     return 0
        # dp = [0] * len(prices)
        # res = 0
        # for i in range(1, len(prices)):
        #     dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
        #     res = max(dp[i], res)
        # return res

sol = Solution()
prices = [7, 1, 3, 2, 6, 5]
print(sol.maxProfite(prices))
