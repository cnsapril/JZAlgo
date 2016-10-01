# coding=utf-8
from ListNode import ListNode, print_list


class Solution:
    def find_k_th(self, head, k):
        for i in xrange(k):
            if head is None:
                return None
            head = head.next
        return head

    def reverse(self, head):
        prev, curt = None, head
        while curt is not None:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev

    def reverse_between(self, head, m, n):
        dummy = ListNode(-1, head)
        pre_m = self.find_k_th(dummy, m-1)
        m_th = pre_m.next
        n_th = self.find_k_th(dummy, n)
        post_n = n_th.next

        n_th.next = None
        self.reverse(m_th)

        pre_m.next = n_th
        m_th.next = post_n
        return dummy.next


sol = Solution()
head = ListNode(3760, ListNode(2881, ListNode(7595, ListNode(3904))))
print_list(sol.reverse_between(head, 1, 2))

