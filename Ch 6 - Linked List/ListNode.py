class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_list(node):
    while node is not None:
        print str(node.val) + " ->",
        node = node.next
    print "null"
