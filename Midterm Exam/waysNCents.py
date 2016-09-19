# coding=utf-8
import sys
class Solution:
    # @param {int} n an integer
    # @return {int} an integer

    def waysNCents(self, n):
        # Write your code here
        coins = [1, 5, 10, 25]

        f = [[0 for i in range(n+1)] for j in range(len(coins))]

        for i in range(n+1):
            f[0][i] = 1

        for j in range(len(coins)):
            f[j][0] = 1

        for i in range(len(coins)):
            for j in range(n+1):
                if j >= coins[i]:
                    f[i][j] = f[i-1][j] + f[i][j-coins[i]]
                else:
                    f[i][j] = f[i-1][j]

        return f[len(coins)-1][n]


sol = Solution()
print sol.waysNCents(11)
