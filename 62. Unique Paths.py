# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

import numpy as np
def uniquePaths(m, n):
    # move = [[1 for _ in range(n)] for _ in range(m)]
    # for i in range(1, m):
    #     for j in range(1, n):
    #         move[i][j] = move[i][j-1] + move[i-1][j]
    # return move[-1][-1]
    k = m - 1
    n = m + n - 2
    res = 1
    for i in range(1, k+1):
        res *= (n - i + 1) / i
    return int(res)
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # discovered = [[0 for _ in range(n)] for _ in range(m)]
    # res = 0
    # movement = [[0, 1],
    #             [-1, 0]]
    # start = [m-1, 0]
    # target = [0, n-1]
    # verticies = [start]
    # while len(verticies) > 0:
    #     [x0, y0] = verticies.pop()
    #     discovered[x0][y0] = 1
    #     for i in range(len(movement)):
    #         x = x0 + movement[i][0]
    #         y = y0 + movement[i][1]
    #         if [x, y] == target:
    #             res += 1
    #         elif x >= 0 and x< m and y>=0 and y<n and discovered[x][y] == 0:
    #             verticies.append([x, y])
    # return res

if __name__ == '__main__':
    m = 3
    n = 3
    res = uniquePaths(m, n)
    print("The result is ", res)