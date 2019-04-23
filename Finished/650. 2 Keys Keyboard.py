class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution 1
        res, i = 0, 2
        while i * i <= n:
            while n % i == 0:
                res += i
                n = n // i
            if i == 2:
                i += 1
            else:
                i += 2

        if n == 1:
            return res
        else:
            return res + n

        # Solution 2
        # dp = [-1]*(n+1)
        # dp[1] = 0
        # dp[2] = 2
        # # for i in range(3, n+1):
        # #     dp[i] = i
        # for i in range(3, n+1):
        #     for j in range(i-1, 1, -1):
        #         if i%j == 0:
        #             dp[i] = dp[j] + i/j
        #             break
        # return dp[-1]

sol = Solution()
print(sol.minSteps(3))

