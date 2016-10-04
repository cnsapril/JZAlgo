# coding=utf-8
import sys


class Solution:
    def minimumTotal(self, triangle):
        if triangle is None or not triangle:
            return sys.maxsize

        length = len(triangle)

        # f[i][j] = 从(0,0)走到(i,j)的最小路径和
        f = [[sys.maxsize for x in range(length)] for y in range(length)]

        # 最左边的那一列只能被它上面的那一格走到 (因为只能向下或向右)
        f[0][0] = triangle[0][0]
        for x in range(1, length):
            f[x][0] = f[x-1][0] + triangle[x][0]

        for i in range(length):
            for j in range(1, i+1):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]

        # 最后的答案为走到最后一行的所有路径和中最小的一个
        return min(f[length-1])


sol = Solution()
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print str(sol.minimumTotal(triangle))