class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or not A:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] == target:
                return mid
            if A[mid] >= A[start]:
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[end] >= target > A[mid]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1


sol = Solution()
print sol.search([2, 3, 4, 0, 1], 4)
