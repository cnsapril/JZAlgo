# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        result = []

        if root is None:
            return result

        queue = [root]
        while queue:
            level = []
            for i in xrange(len(queue)):
                head = queue.pop(0)
                level.append(head.val)
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
            result.append(level)

        return result

sol = Solution()
root = TreeNode(1)
nodel = TreeNode(2)
noder = TreeNode(3)
root.left = nodel
root.right = noder
print sol.levelOrder(root)
