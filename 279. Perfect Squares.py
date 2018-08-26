class Solution:
    def numSquares(self, n):
        """
        Given a positive integer n, find the least number of perfect square numbers
        (for example, 1, 4, 9, 16, ...) which sum to n.
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        dp = [float('Inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[n]

import cProfile
sol = Solution()
cProfile.run(sol.numSquares(7217))