# coding=utf-8
class Solution:
    def longestCommonSubsequence(self, A, B):
        if A is None or B is None or not A or not B:
            return 0

        len_a = len(A)
        len_b = len(B)

        # f[i][j] 表示A的前i个字符与B的前j个字符的最长公共子序列的长度
        f = [[0 for i in range(len_b+1)] for j in range(len_a+1)]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i-1][j-1]+1, f[i-1][j], f[i][j-1])
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])

        return f[len_a][len_b]


sol = Solution()
print str(sol.longestCommonSubsequence("ABCD", "EB"))