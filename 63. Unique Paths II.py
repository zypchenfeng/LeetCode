class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)  
        
        if not m:              # check if the grid is empty   
            return 0
        
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)] # initialize dp

        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1 # check if the starting point is blocked

        for i in range(1, m):               
            dp[i][0] = dp[i-1][0]*(1 - obstacleGrid[i][0])  # for the first row, if any space is blocked, the grid after that are all zero
        for i in range(1, n):
            dp[0][i] = dp[0][i-1]*(1 - obstacleGrid[0][i])  # for the first column, if any space is blocked, the grid after that are all zero        
        for i in range(1, m):
            for j in range(1, n): 
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])*(1-obstacleGrid[i][j]) # go over the entire grid
        return dp[-1][-1]

sol = Solution()
obstacleGrid = [
  [0,0,0,0],
  [1,0,1,1],
  [0,0,0,0],
  [0,1,0,0],
  [0,0,0,0]
]
print(sol.uniquePathsWithObstacles(obstacleGrid))
print(sol.uniquePathsWithObstacles([[0],[1]]))
print(sol.uniquePathsWithObstacles([[0, 1]]))
print(sol.uniquePathsWithObstacles([[1, 0], [0, 0]]))
print(sol.uniquePathsWithObstacles([]))