class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def preorderTreversal_Iteration(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result

    def preorderTraversal_DFS(self, root):
        def helper(root, result):
            if root is None:
                return

            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)

        result = []
        helper(root, result)
        return result

    def preorderTraversal_DAC(self, root):
        if root is None:
            return []

        left = self.preorderTraversal_DAC(root.left)
        right = self.preorderTraversal_DAC(root.right)
        result = [root.val]
        result.extend(left)
        result.extend(right)

        return result

    def inorderTraversal(self, root):
        if root is None:
            return []

        stack = []
        result = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result


root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root.left = node1
root.right = node2
node2.left = node3
sol = Solution()
print sol.inorderTraversal(root)
