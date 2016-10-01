from ListNode import ListNode, print_list


class Solution:
    def getLength(self, head):
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length

    def rotateRight(self, head, k):
        if head is None:
            return None

        length = self.getLength(head)
        k = k % length

        dummy = ListNode(0, head)
        tail = dummy
        node = dummy

        for i in xrange(k):
            node = node.next

        while node.next is not None:
            node = node.next
            tail = tail.next

        node.next = dummy.next
        dummy.next = tail.next
        tail.next = None

        return dummy.next


sol = Solution()
print_list(sol.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))


