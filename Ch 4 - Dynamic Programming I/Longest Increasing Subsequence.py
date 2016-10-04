# coding=utf-8
class Solution:
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0

        length = len(nums)

        # f[i]表示从0到i的最长子序列
        f = [1 for i in range(length)]

        f[0] = 1
        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)


sol = Solution()
nums = [88, 4, 24, 82, 86, 1, 56]
print str(sol.longestIncreasingSubsequence(nums))
