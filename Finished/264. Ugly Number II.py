class Solution:
    def nthUglyNumber(self, n):
        """
        Write a program to find the n-th ugly number.
        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
        :type n: int
        :rtype: int
        """
        # solution 2 faster
        if n == 1: return 1
        dp = [1]*n
        t2 = t3 = t5 = 0
        for i in range(1, n):
            dp[i] = min(dp[t2]*2, dp[t3]*3, dp[t5]*5 )
            if dp[i] == dp[t2] * 2:
                t2 += 1
            if dp[i] == dp[t3] * 3:
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1

        return dp[n-1]


        #solution 1 extremely slow
    #     ugly = {}
    #     i = 1
    #     counter = 1
    #     while counter <= n:
    #         if self.check_ugly(i):
    #             ugly[str(counter)] = i
    #             counter += 1
    #         i += 1
    #     return ugly.get(str(n))
    #
    # def check_ugly(self, n):
    #     noms = [2, 3, 5]
    #     res = True
    #     while n>1:
    #         temp = n
    #         for nom in noms:
    #             if n%nom == 0:
    #                 n /= nom
    #                 break
    #         if temp == n:
    #             return False
    #     if n == 1.0:
    #         return True
    #     else:
    #         return False

sol = Solution()
print(sol.nthUglyNumber(10))
print(sol.nthUglyNumber(2))
print(sol.nthUglyNumber(4))
print(sol.nthUglyNumber(1689))