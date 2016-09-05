"""
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""


class Solution(object):
    def permute_unique(self, nums):
        def _permute(result, temp, nums):
            if not nums:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i and nums[i] == nums[i-1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])
        if nums is None:
            return []
        result = []
        _permute(result, [], sorted(nums))
        return result


sol = Solution()
print sol.permute_unique([1, 1, 2, 3])
