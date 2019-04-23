class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp =[0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

sol = Solution()
print(sol.climbStairs(1))
print(sol.climbStairs(3))
print(sol.climbStairs(10))
print(sol.climbStairs(100))