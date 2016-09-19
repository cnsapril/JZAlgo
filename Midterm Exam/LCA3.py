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

            if left[0] or left[1]:
                return left

            if right[0] or right[1]:
                return right

            return False, False, None

        result = helper(root, A, B)
        return result[2]

# {9,3,#,0,#,-4,#,-16,#,-18,-7,-63}

sol = Solution()
n9 = TreeNode(9)
n3 = TreeNode(3)
n0 = TreeNode(0)
n_4 = TreeNode(-4)
n_16 = TreeNode(-16)
n_18 = TreeNode(-18)
n_7 = TreeNode(-7)
n_63 = TreeNode(-63)

n9.left = n3
n3.left = n0
n0.left = n_4
n_4.left = n_16
n_16.left, n_16.right = n_18, n_7
n_18.left = n_63

result = sol.lowestCommonAncestor3(n9, n_63, n3)
print result.val
