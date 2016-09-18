# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __eq__(self, other):
        return self.val == other.val

import copy


class Solution:
    """
    @param {TreeNode} root The root of the binary tree.
    @param {TreeNode} A and {TreeNode} B two nodes
    @return Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        def helper(root, A, B):
            if root is None:
                return False, False, None

            left = helper(root.left, A, B)
            right = helper(root.right, A, B)

            if root == A and root == B:
                return True, True, root

            if root == A and (left[1] or right[1]):
                return True, True, root

            if root == B and (left[0] or right[0]):
                return True, True, root

            if left[2] is not None and right[2] is not None:
                return True, True, root

            if left[2] is not None:
                return left

            if right[2] is not None:
                return right

            if root == A:
                return True, False, None

            if root == B:
                return False, True, None

            if (left[0] and right[1]) or (left[1] and right[0]):
                return root

            return False, False, None

        result = helper(root, A, B)
        return result[2]


sol = Solution()
root = TreeNode(1)
nodel = TreeNode(2)
noder = TreeNode(3)
root.left = nodel
root.right = noder

result = sol.lowestCommonAncestor3(root, nodel, noder)
print result