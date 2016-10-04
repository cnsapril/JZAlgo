# coding=utf-8
class Solution:
    def numDistince(self, S, T):
        if S is None:
            return 0

        len_s = len(S)
        len_t = len(T)

        # f[i][j] 表示S中前i个字符的子序列中出现了多少次T中前j个字符
        f = [[0 for i in xrange(len_t+1)] for j in xrange(len_s+1)]

        for i in xrange(len_s + 1):
            f[i][0] = 1

        for i in xrange(1, len_s+1):
            for j in xrange(1, len_t+1):
                f[i][j] = f[i-1][j]
                if S[i-1] == T[j-1]:
                    f[i][j] += f[i-1][j-1]

        return f[len_s][len_t]


sol = Solution()
print str(sol.numDistince("apple", "ple"))
