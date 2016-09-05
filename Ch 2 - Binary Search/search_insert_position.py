"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.
"""


class Solution(object):
    def search_insert(self, A, target):
        if not A:
            return 0

        left, right = 0, len(A) - 1
        if target > A[right]:
            return right + 1
        if target < A[left]:
            return left

        while left + 1 < right:
            m = left + (right - left)/2
            if A[m] == target:
                return m
            elif A[m] > target:
                right = m
            else:
                left = m

        if target == A[left]:
            return left
        elif target == A[right]:
            return right
        else:
            return right


sol = Solution()
print sol.search_insert([1, 2, 3, 5], 0)
