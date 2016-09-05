class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if A is None or not A:
            return []

        start, end = 0, len(A) - 1
        index = -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        count = 0

        i, j = start, end
        rst = []

        while count < k:
            if i >= 0 and j <= len(A) - 1:
                if abs(A[i] - target) <= abs(A[j] - target):
                    rst.append(A[i])
                    i -= 1
                else:
                    rst.append(A[j])
                    j += 1
            elif j <= len(A) - 1:
                rst.append(A[j])
                j += 1
            elif i >= 0:
                rst.append(A[i])
                i -= 1
            else:
                break
            count += 1

        return rst


sol = Solution()
print sol.kClosestNumbers([1,4,6,8],3,3)
