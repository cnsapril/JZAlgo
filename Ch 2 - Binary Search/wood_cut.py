class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        # write your code here
        if L is None or not L:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            count = sum([x / mid for x in L])
            if count < k:
                end = mid
            elif count > k:
                start = mid
            else:
                start = mid

        if sum([x / end for x in L]) >= k:
            return end
        if sum([x / start for x in L]) >= k:
            return start

        return 0


sol = Solution()
print sol.woodCut([232, 124, 456], 7)
