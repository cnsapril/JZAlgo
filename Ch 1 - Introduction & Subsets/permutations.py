"""
Given a list of numbers, return all possible permutations.
You can assume that there is no duplicate numbers in the list.
"""


class Solution(object):
    def permute(self, nums):
        def _permute(result, temp, nums):
            if not nums:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])
        if nums is None:
            return []
        result = []
        _permute(result, [], nums)
        return result


sol = Solution()
print sol.permute([1, 3, 2])

