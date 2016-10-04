# coding=utf-8
import sys


class Solution:
    def minDistance(self, word1, word2):
        if word1 is None and word2 is None:
            return sys.maxsize
        if word1 is None or not word1:
            return len(word2)
        if word2 is None or not word2:
            return len(word1)

        len1 = len(word1)
        len2 = len(word2)

        # f[i][j] 表示将第一个单词的前i个字母变成第二个单词的前j个字母最少需要多少个操作
        f = [[sys.maxsize for i in range(len2+1)] for j in range(len1+1)]

        for i in range(len1+1):
            f[i][0] = i

        for j in range(len2+1):
            f[0][j] = j

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] != word2[j-1]:
                    # 如果不相等,可进行的操作有:
                    # 1. 删除word1的最后一个字符: f[i-1][j] + 1
                    # 2. 在word1的后面插入一个字符: f[i][j-1] + 1
                    # 3. 讲word1[i]替换为word2[j]: f[i-1][j-1] + 1
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
                else:
                    # 如果相等,可进行的操作有:
                    # 1. 不管: f[i-1][j-1]
                    # 2. 删除word1最后一个字符: f[i-1][j] + 1
                    # 3. 插入一个字符: f[i][j-1] + 1
                    f[i][j] = min(f[i-1][j-1], f[i-1][j] + 1, f[i][j-1] + 1)

        return f[len1][len2]


sol = Solution()
print sol.minDistance("asdh", "dajssa")
