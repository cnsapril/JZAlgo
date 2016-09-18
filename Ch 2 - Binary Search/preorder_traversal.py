class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class Solution:
    # Pre-order traversal using recursion
    def preorderTraversal(self, root):
        def helper(root, rst):
            if root is None:
                return

            rst.append(root.value)
            helper(root.left, rst)
            helper(root.right, rst)

        rst = []
        helper(root, rst)
        return rst

    # Pre-order traversal using divide and conquer
    def preorder_traversal_divide_and_conquer(self, root):
        if root is None:
            return []

        left = self.preorder_traversal_divide_and_conquer(root.left)
        right = self.preorder_traversal_divide_and_conquer(root.right)
        rst = [root.value]
        rst.extend(left)
        rst.extend(right)
        return rst

sol = Solution()
root = TreeNode(1)
nodel = TreeNode(2)
noder = TreeNode(3)
root.left = nodel
root.right = noder

print sol.preorder_traversal_divide_and_conquer(root)
