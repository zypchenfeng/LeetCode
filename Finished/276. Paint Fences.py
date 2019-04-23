class Solution(object):
    def waysToPaint(self, n, k):
        '''
        :param n: non-negative, number of posts to be painted
        :param k: non-negative, number of colors to choose from
        :return: total number of ways to paint when no more than 2 nearby posts with the same color
        '''
        if not n or not k:
            return 0
        if n == 1:
            return k
        dp = [k]*n
        dp[1] = k + k*(k-1)
        for i in range(2, n):
            dp[i] = (dp[i-2] + dp[i-1])*(k-1)
        return dp[-1]

sol = Solution()
n = 2
k = 2
print(sol.waysToPaint(n, k))

n = 0
k = 0
print(sol.waysToPaint(n, k))

n = 1
k = 1
print(sol.waysToPaint(n, k))

n = 3
k = 4
print(sol.waysToPaint(n, k))