from ListNode import ListNode


class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None

        slow, fast = head, head.next
        while fast != slow:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next

        while head != slow.next:
            head = head.next
            slow = slow.next

        return head


sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3
head = node1

node = sol.detectCycle(head)
print node.val
