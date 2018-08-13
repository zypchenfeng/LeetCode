"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

class Solution:
    def swimInWater(self, grid):

"""
def swimInWater(grid):
    time = grid[0][0]
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    start = [0, 0]
    target = [len(grid)-1, len(grid)-1]
    Q = [[time, start[0], start[1]]]
    direction = [[1, 0],
                 [0, 1],
                 [-1, 0],
                 [0, -1]] # all the directions it can go
    while len(Q) > 0:
        Q.sort(reverse = True)
        t, x0, y0 = Q.pop()
        t = max(time, t)
        for i in range(len(direction)):
            x = x0 + direction[i][0]
            y = y0 + direction[i][1]
            if x>=0 and x<len(grid[0]) and y>=0 and y<len(grid) and visited[x][y] == 0:
                visited[x][y] = 1
                temp = max(t, grid[x][y])
                if x == target[0] and y == target[1]:
                    return max(t, grid[x][y])
                else:
                    Q.append([temp, x, y])

# grid = [[10,12, 4,  6],
#         [9, 11, 3,  5],
#         [1,  7, 13, 8],
#         [2,  0, 15, 14]]
# grid = [[7,11,5,3],
#         [2,14,12,8],
#         [4,13,9,10],
#         [6,0,1,15]]
grid =[[0,  1,  2,  3,  4],
        [24, 23, 22, 21,  5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 16],
        [10,  9,  8,  7,  6]]
print(swimInWater(grid))

