# coding=utf-8
class Solution:

    # 动态规划算法,时间复杂度为O(n^2),在lintcode上会超时,但是仍然需要掌握
    def canJump(self, A):
        if A is None or not A:
            return False

        length = len(A)

        # f[i] 表示从第0格跳到第i格是否能成功
        f = [False for x in range(length)]

        f[0] = True

        # 对第i格来说,如果能够在0到(i-1)格中找到能够被跳到的一格(f[j] == True),
        # 且那一个能够跳到i格(A[j] >= (i-j)),那么i格是可以被跳到的
        for i in range(1, length):
            for j in range(i):
                if f[j] and A[j] >= (i-j):
                    f[i] = True
                    break

        return f[length-1]

    # 贪心算法,时间复杂度O(n)
    def canJump_greedy(self, A):
        if A is None or not A:
            return False

        length = len(A)
        farthest = A[0]

        for i in range(1, length):
            if i <= farthest <= A[i] + i:
                farthest = A[i] + i

        return farthest >= length - 1


sol = Solution()
A = [3, 2, 1, 0, 4]
print sol.canJump_greedy(A)
