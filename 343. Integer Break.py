class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = (n+1)*[1]
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j])*max((i-j), dp[i-j]))
        return dp[-1]

sol = Solution()
print(sol.integerBreak(10))
print(sol.integerBreak(2))