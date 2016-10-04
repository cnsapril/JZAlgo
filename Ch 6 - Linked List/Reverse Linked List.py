from ListNode import ListNode, print_list


class Solution:
    def reverse(self, head):
        prev, curt = None, head
        while curt is not None:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev


sol = Solution()
node1 = ListNode(1, ListNode(2, ListNode(3)))
head = node1
print_list(head)
print_list(sol.reverse(head))
