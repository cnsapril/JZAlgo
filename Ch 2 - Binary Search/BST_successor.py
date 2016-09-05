# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    # Own answer: traverse the whole tree to generate the list
    def inorderSuccessor(self, root, p):
        # write your code here
        def helper(root):
            if root is None:
                return []

            left = helper(root.left)
            right = helper(root.right)

            rst = []
            rst.extend(left)
            rst.append(root)
            rst.extend(right)

            return rst

        lst = helper(root)
        for i in range(len(lst)-1):
            node = lst[i]
            if node.val == p.val:
                return lst[i+1]

        return None

    # Answer from JZAlgo (in-order traversal of a BST is ascending)
    def inorder_successor(self, root, p):
        if root is None or p is None:
            return None

        successor = None
        while root is not None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root is None:
            return None

        if root.right is None:
            return successor

        root = root.right
        while root.left is not None:
            root = root.left
        return root


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2

sol = Solution()
print sol.inorder_successor(root, root).val
