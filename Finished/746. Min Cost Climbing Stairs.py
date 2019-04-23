class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n < 3:
            return min(cost)
        dp = [0] * (n+1)
        cost = [0] + cost
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-1], dp[i-1] + cost[i])
        return dp[-1]
sol = Solution()
cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost2 = [10, 15, 20]
cost3 = [1, 2]
cost4 = [0, 0, 1, 1]

print(sol.minCostClimbingStairs(cost1))
print(sol.minCostClimbingStairs(cost2))
print(sol.minCostClimbingStairs(cost3))
print(sol.minCostClimbingStairs(cost4))