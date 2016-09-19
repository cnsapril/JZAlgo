class Solution:
    """
    @param {int} n a integer
    @return {int} a integer
    """
    def climbStairs2(self, n):
        # Write your code here
        f = [1, 1, 2, 4]
        for i in range(4, n+1):
            f.append(f[i-1] + f[i-2] + f[i-3])

        return f[n]


sol = Solution()
print sol.climbStairs2(10)
