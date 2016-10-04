# coding=utf-8
import sys


class Solution:
    def minPathSum(self, grid):
        if grid is None or not grid:
            return sys.maxsize

        m = len(grid)
        n = len(grid[0])

        # f[i][j] 代表从(0,0)走到(i,j)的最小路径和
        f = [[sys.maxsize for x in range(n)] for y in range(m)]

        f[0][0] = grid[0][0]
        for i in range(1, m):
            f[i][0] = f[i-1][0] + grid[i][0]

        for j in range(1, n):
            f[0][j] = f[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]

        return f[m-1][n-1]


sol = Solution()
grid = [
    [1, 3, 5],
    [0, 2, 3],
    [-1, 2, 1]
]
print sol.minPathSum(grid)
