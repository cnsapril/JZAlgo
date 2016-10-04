from ListNode import ListNode, print_list


class Solution:
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        prev, curt = None, head
        while curt is not None:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev

    def merge(self, head1, head2):
        dummy = ListNode(0)
        index = 0

        while head1 is not None and head2 is not None:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            index += 1
            dummy = dummy.next

        if head1 is not None:
            dummy.next = head1
        else:
            dummy.next = head2

    def reorderList(self, head):
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        reversed_head = self.reverse(mid.next)
        mid.next = None

        self.merge(head, reversed_head)


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reorderList(head)
print_list(head)
