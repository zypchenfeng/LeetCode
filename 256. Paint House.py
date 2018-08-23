class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        There are a row of n houses, each house can be painted with one of the three colors:
        red, blue or green. The cost of painting each house with a certain color is different.
        You have to paint all the houses such that no two adjacent houses have the same color.
        The cost of painting each house with a certain color is represented by a n x 3 cost
        matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2]
        is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint
        all houses.
        """
        if not costs or len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0]*3]*n
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[n-1])

sol = Solution()
costs =[[1, 2, 3],
        [3, 2, 1],
        [3, 2, 3]]
print(sol.minCost(costs))