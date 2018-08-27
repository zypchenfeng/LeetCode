class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # idea: dp: matrix for the map, dp value is the unique path until this point. Runtime: O(mn)
        #           Difference with original map: when the node is obstacle, the dp value of it is 0
        m = len(obstacleGrid)
        if not m:
            return 0
        n = len(obstacleGrid[0])
        
        # if there is obstacle in start point, dp value is 0. else dp value is 1
        obstacleGrid[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        # for the first column, write all the dp values from the previous value, change obstacle position dp to 0
        for i in range(1,m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] if obstacleGrid[i][0] != 1 else 0
        # for the first row, write all the dp values from the previous value, change obstacle position dp to 0
        for i in range(1,n):
            obstacleGrid[0][i] = obstacleGrid[0][i-1] if obstacleGrid[0][i] != 1 else 0
        
        # search all the map, change obstacle position dp to 0, for position with no obstable, just add from left and top
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]