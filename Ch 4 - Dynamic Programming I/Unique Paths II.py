class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None or not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        f = [[0 for i in range(n)] for j in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        f[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                f[i][0] = 0
            else:
                f[i][0] = f[i-1][0]

        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                f[0][j] = 0
            else:
                f[0][j] = f[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]


sol = Solution()
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print str(sol.uniquePathsWithObstacles(grid))
