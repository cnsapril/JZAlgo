# coding=utf-8
class Solution:
    def wordBreak(self, s, dict):
        if s is None or dict is None:
            return False

        length = len(s)

        # f[i] 表示前i个字符能否被完美切分
        f = [False] * (length + 1)
        f[0] = True

        max_length = max([len(x) for x in dict])

        for i in xrange(1, length + 1):
            for j in range(max(0, i-max_length), i):
                if not f[j]:
                    continue
                if s[j:i] in dict:
                    f[i] = True
                    break

        return f[length]


sol = Solution()
dict = ["lint", "code"]
print sol.wordBreak("lintcode", dict)