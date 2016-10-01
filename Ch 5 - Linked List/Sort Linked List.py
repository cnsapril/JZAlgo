from ListNode import ListNode, print_list


class Solution:
    # Implemented using Merge sort. However, quick sort can also be applied.
    # Relevant answer: http://www.jiuzhang.com/solutions/sort-list/
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1 is not None:
            tail.next = head1
        else:
            tail.next = head2

        return dummy.next

    def sortList(self, head):
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(left, right)


sol = Solution()
print_list(sol.sortList(ListNode(3, ListNode(1, ListNode(5, ListNode(2))))))
