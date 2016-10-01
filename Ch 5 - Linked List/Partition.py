from ListNode import ListNode, print_list


class Solution:
    def partition(self, head, x):
        left_head = ListNode(-1)
        right_head = ListNode(-1)
        left_tail, right_tail = left_head, right_head

        node = head
        while node is not None:
            if node.val < x:
                left_tail.next = node
                left_tail = left_tail.next
            else:
                right_tail.next = node
                right_tail = right_tail.next
            node = node.next

        right_tail.next = None
        left_tail.next = right_head.next

        return left_head.next


sol = Solution()
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print_list((sol.partition(head, 3)))


