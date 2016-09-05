import sys


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        def helper(root):
            if root is None:
                return -sys.maxint, 0

            left = helper(root.left)
            right = helper(root.right)

            any2any = max(left[0], right[0])
            root2any = max(0, max(left[1], right[1])) + root.val

            cross_root = left[1] + root.val + right[1]
            any2any = max(any2any, root2any, cross_root)
            return any2any, root2any

        result = helper(root)
        return result[0]


root = TreeNode(1)
node1l = TreeNode(2)
node1r = TreeNode(3)
root.left = node1l
root.right = node1r
sol = Solution()
print sol.maxPathSum(root)
