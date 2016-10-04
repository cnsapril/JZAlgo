from ListNode import ListNode, print_list


class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False


sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
head = node1
print str(sol.hasCycle(head))
