"""
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n)
time complexity.

If the target number does not exist in the array, return -1.
"""


class Solution(object):
    def binary_search(self, nums, target):
        if not nums or nums is None:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] == target and nums[mid-1] != target:
                return mid
            elif nums[mid] >= target:
                end = mid
            elif nums[mid] <= target:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


sol = Solution()
print sol.binary_search([1, 1, 1, 2, 2, 3, 3], 2)
