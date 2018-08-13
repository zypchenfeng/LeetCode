class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not len(grid):
            return 0
        res = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    self.dfs(grid, m, n)
                    res += 1
        return res
    def dfs(self, grid, m, n):
        if m>=0 and m<len(grid) and n>=0 and n<len(grid[0]) and grid[m][n] == '1':
            grid[m][n] = '#'
            self.dfs(grid, m-1, n)
            self.dfs(grid, m+1, n)
            self.dfs(grid, m, n-1)
            self.dfs(grid, m, n+1)
        else:
            return

grid = []
# grid = [[1,1,1,1,0],
#         [1,1,0,1,0],
#         [1,1,0,0,0],
#         [0,0,0,0,0]]

print('Number of islands in the grid is', num_islands(grid))