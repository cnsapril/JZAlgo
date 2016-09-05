"""
Given a list of numbers that may has duplicate numbers, return all possible subsets
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.
"""


class Solution(object):
    def subsets_with_dup(self, s):
        def _subsets(result, temp, nums, pos):
            result += [temp]
            for i in range(pos, len(nums)):
                if i and nums[i] == nums[i-1]:
                    continue
                _subsets(result, temp + [nums[i]], nums, i+1)
        if s is None:
            return []
        result = []
        _subsets(result, [], sorted(s), 0)
        return result


sol = Solution()
print sol.subsets_with_dup([1, 2, 2, 3, 3, 4, 3])
