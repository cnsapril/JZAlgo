# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    # Divide and conquer
    def isValidBST(self, root):
        # write your code here
        def helper(root):
            if root is None:
                return [], True

            left = helper(root.left)
            right = helper(root.right)

            if not left[1] or not right[1]:
                return [], False

            if left[0]:
                if left[0][-1] >= root.val:
                    return [], False

            if right[0]:
                if right[0][0] <= root.val:
                    return [], False

            rst = []
            rst.extend(left[0])
            rst.append(root.val)
            rst.extend(right[0])
            return rst, True

        return helper(root)[1]

    # DFS
    def validate(self, root):
        if root is None:
            return

        self.validate(root.left)
        if self.lastValue is not None and self.lastValue >= root.val:
            self.isBST = False
            return
        self.lastValue = root.val
        self.validate(root.right)

    def is_valid_BST(self, root):
        self.isBST = True
        self.lastValue = None
        self.validate(root)
        return self.isBST


root = TreeNode(10)
node1l = TreeNode(5)
node1r = TreeNode(15)
node2l = TreeNode(6)
node2r = TreeNode(20)
root.left = node1l
root.right = node1r
node1r.left = node2l
node1r.right = node2r

sol = Solution()
print sol.is_valid_BST(root)
