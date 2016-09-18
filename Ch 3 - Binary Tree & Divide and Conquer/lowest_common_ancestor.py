#Definition of TreeNode:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    # Own answer - time complexity is the same, but overlap of conditions
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        def helper(root, A, B):
            if root is None:
                return False, None

            left = helper(root.left, A, B)
            right = helper(root.right, A, B)

            if left[0]:
                return left

            if right[0]:
                return right

            if (left[1] == A and right[1] == B) or (left[1] == B and right[1] == A):
                return True, root

            if (left[1] == A and root == B) or (left[1] == B and root == A) or (right[1] == A and root == B) or (
                    right[1] == B and root == A):
                return True, root

            if left[1] is not None:
                return left

            if right[1] is not None:
                return right

            if root == A or root == B:
                return False, root

            return False, None

        result = helper(root, A, B)
        return result[1]

    def lowest_common_ancestor(self, root, A, B):
        if root is None:
            return None

        if root == A or root == B:
            return root

        left = self.lowest_common_ancestor(root.left, A, B)
        right = self.lowest_common_ancestor(root.right, A, B)

        if left is not None and right is not None:
            return root

        if left is not None:
            return left

        if right is not None:
            return right

        return None


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
root.right = node2
node2.right = node3
node3.right = node4
node4.right = node5
sol = Solution()
rst = sol.lowest_common_ancestor(root, node3, node5)
print rst.val
