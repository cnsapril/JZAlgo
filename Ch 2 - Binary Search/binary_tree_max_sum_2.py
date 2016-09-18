"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        if root is None:
            return 0

        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)

        # The values could be negative. If the max value of the subtrees is negative,
        # just return the value of the root
        return max(0, max(left, right)) + root.val

root = TreeNode(1)
nodel = TreeNode(2)
noder = TreeNode(3)
root.left = nodel
root.right = noder

sol = Solution()
print sol.maxPathSum2(root)