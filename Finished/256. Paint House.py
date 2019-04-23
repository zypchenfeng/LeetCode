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
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        for i in range(len(costs)):
            for j in range(3):
                dp[i][j] = min(dp[i-1][k] for k in range(3) if k != j) + costs[i][j]
        return min(dp[-1])

sol = Solution()
costs =[[1, 2, 3],
        [3, 2, 1],
        [3, 2, 3]]
print(sol.minCost(costs))




























