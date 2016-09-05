"""
Given a set of distinct integers, return all possible subsets.
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
"""


class Solution(object):
    def subsets(self, s):
        def _subsets(result, temp, nums, pos):
            result += [temp]
            for i in range(pos, len(nums)):
                _subsets(result, temp + [nums[i]], nums, i+1)
        if s is None:
            return []
        result = []
        _subsets(result, [], sorted(s), 0)
        return result


sol = Solution()
print sol.subsets([1, 3, 2])
