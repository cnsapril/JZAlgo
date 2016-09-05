"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        def helper(root):
            if root is None:
                return True, 0

            left = helper(root.left)
            right = helper(root.right)

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return True, max(left[1], right[1]) + 1
            else:
                return False, 0

        balanced, _ = helper(root)
        return balanced
