# coding=utf-8
class Solution:
    def uniquePaths(self, m, n):

        # f[i][j] 代表从(0,0)走到(i,j)有多少种不同的方法
        f = [[0 for i in range(n)] for j in range(m)]

        # 初始化: 最左列和第一行均只能通过一直往下走或一直往右走到达
        for i in range(m):
            f[i][0] = 1

        for j in range(n):
            f[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i-1][j] + f[i][j-1]

        return f[m-1][n-1]


sol = Solution()
print sol.uniquePaths(30, 30)
