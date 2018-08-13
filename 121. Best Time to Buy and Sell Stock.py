class Solution(object):
    def maxProfire(self, prices):
        if len(prices) < 2:
            return 0
        dp = [0] * len(prices)
        res = 0
        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
            res = max(dp[i], res)
        return res

sol = Solution()
prices = [7, 6, 3, 2, 6, 5]
print(sol.maxProfire(prices))
