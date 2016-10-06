# coding=utf-8
class Solution():
    def isInterleave(self, s1, s2, s3):
        if s1 is None or s2 is None or s3 is None:
            return False

        if not s3:
            return not s1 and not s2

        if not s1:
            return s2 == s3

        if not s2:
            return s1 == s3

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 + len_s2 != len(s3):
            return False

        # f[i][j] 表示s3是否由s1的前i个字符和s2的前j个字符交替组成
        f = [[False for i in range(len_s2 + 1)] for j in \
             range(len_s1 + 1)]

        for i in range(len_s1 + 1):
            f[i][0] = s1[:i] == s3[:i]

        for j in range(len_s2 + 1):
            f[0][j] = s2[:j] == s3[:j]

        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                f[i][j] = (f[i-1][j] and (s1[i-1] == s3[i+j-1])) or (f[i][j-1] and (s2[j-1] == s3[i+j-1]))

        return f[len_s1][len_s2]


sol = Solution()
s1 = "abc"
s2 = "de"
s3 = "abdce"
print str(sol.isInterleave(s1, s2, s3))
