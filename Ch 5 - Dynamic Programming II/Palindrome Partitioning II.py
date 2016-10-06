import sys


class Solution:
    def is_palindrome(self, s):
        length = len(s)
        p = [[False for i in range(length)] for j in range(length)]

        for i in range(length):
            p[i][i] = True

        for i in range(length - 1):
            p[i][i+1] = (s[i] == s[i+1])

        for l in range(2, length + 1):
            for start in range(0, length - l):
                p[start][start+l] = p[start+1][start+l-1] and (s[start] == s[start+l])

        return p

    def minCut(self, s):
        if s is None or not s:
            return 0

        length = len(s)

        f = [(i - 1) for i in range(length + 1)]
        is_p = self.is_palindrome(s)

        for i in range(1, length+1):
            for j in range(i):
                if is_p[j][i-1]:
                    f[i] = min(f[i], f[j] + 1)

        return f[length]


sol = Solution()
print sol.minCut("aba")
