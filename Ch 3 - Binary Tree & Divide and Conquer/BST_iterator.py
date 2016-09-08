# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    # @param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.curt = root
        self.stack = []

    # @return: True if there has next node, or false
    def hasNext(self):
    # write your code here
        return self.curt is not None or len(self.stack) > 0


    # @return: return next node
    def next(self):
        # write your code here
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left

        self.curt = self.stack.pop(0)
        nxt = self.curt
        self.curt = self.curt.right
        return nxt

