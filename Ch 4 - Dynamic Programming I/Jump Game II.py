# coding=utf-8
import sys


class Solution:

    # 动态规划算法,时间复杂度O(n^2),超时
    def jump(self, A):
        if A is None or not A:
            return sys.maxsize

        length = len(A)

        # f[i] 表示从第0格跳到第i格所需的最小步数
        f = [sys.maxsize for i in range(length)]
        f[0] = 0

        for i in range(1, length):
            min_step = sys.maxsize
            for j in range(i):
                if f[j] != sys.maxsize and A[j] >= (i-j):
                    min_step = min(min_step, f[j])
            f[i] = min_step + 1

        return f[length-1]

    # 贪心算法 - 不断更新能够跳到的最远区间, 在当前所在位置之前的位置从前到后寻找能够一步跳到当前位置的位置
    def jump_greedy(self, A):
        if A is None or not A:
            return sys.maxsize

        destination = len(A) - 1
        jump = 0

        while destination != 0:
            for i in range(destination):
                if i + A[i] >= destination:
                    destination = i
                    jump += 1
                    break

        return jump



sol = Solution()
A = [2, 3, 1, 1, 4]
print sol.jump_greedy(A)
