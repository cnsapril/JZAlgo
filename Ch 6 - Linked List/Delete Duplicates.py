from ListNode import ListNode, print_list


class Solution:
    """
    @:param head: A ListNode
    @:return: A ListNode
    """
    def remove_duplicates(self, head):
        dummy = ListNode(0, head)
        prev, curt = dummy, dummy.next

        while curt is not None and curt.next is not None:
            if curt.val == curt.next.val:
                val = curt.val
                while curt is not None and curt.val == val:
                    curt = curt.next
                prev.next = curt
            else:
                prev = curt
                curt = curt.next

        return dummy.next


sol = Solution()
node3 = ListNode(3)
node2 = ListNode(2, node3)
node13 = ListNode(1, node2)
node12 = ListNode(1, node13)
node11 = ListNode(1, node12)
head = node11
print_list(sol.remove_duplicates(head))
