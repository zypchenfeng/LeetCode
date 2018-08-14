class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n > 4:   # if n = 4, *4 = *2*2
            n -= 3
            res *= 3
        return n*res


        # Solution 2
        # dp = (n+1)*[1]
        # for i in range(2, n+1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], max(j, dp[j])*max((i-j), dp[i-j]))
        # return dp[-1]

sol = Solution()
print(sol.integerBreak(10))
print(sol.integerBreak(2))
print(sol.integerBreak(4))