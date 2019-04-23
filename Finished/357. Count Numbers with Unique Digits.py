class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        dp = [0]*n
        for i in range(1, n):
            dp[i] = dp[i-1] + 9*10**(i-1)
        return 10**n - dp[n-1]

sol = Solution()
print(sol.countNumbersWithUniqueDigits(1))
print(sol.countNumbersWithUniqueDigits(2))
print(sol.countNumbersWithUniqueDigits(3))
print(sol.countNumbersWithUniqueDigits(4))