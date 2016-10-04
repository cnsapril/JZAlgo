from ListNode import ListNode, print_list
from Queue import PriorityQueue


class Solution:
    # ######################## Merge Sort ######################## #
    # def mergeTwoLists(self, list1, list2):
    #     dummy = ListNode(0)
    #     tail = dummy
    #
    #     while list1 is not None and list2 is not None:
    #         if list1.val < list2.val:
    #             tail.next = list1
    #             list1 = list1.next
    #         else:
    #             tail.next = list2
    #             list2 = list2.next
    #         tail = tail.next
    #
    #     if list1 is not None:
    #         tail.next = list1
    #     else:
    #         tail.next = list2
    #
    #     return dummy.next
    #
    # def mergeHelper(self, lists, start, end):
    #     if start == end:
    #         return lists[start]
    #
    #     mid = start + (end - start) / 2
    #     left = self.mergeHelper(lists, start, mid)
    #     right = self.mergeHelper(lists, mid+1, end)
    #     return self.mergeTwoLists(left, right)
    #
    # def mergeKLists(self, lists):
    #     if lists is None or not lists:
    #         return None
    #
    #     return self.mergeHelper(lists, 0, len(lists)-1)

    # ######################## Heap Sort ######################## #
    # def mergeKLists(self, lists):
    #     if lists is None or not lists:
    #         return None
    #
    #     heap = PriorityQueue()
    #     for node in lists:
    #         if node is not None:
    #             heap.put((node.val, node))
    #
    #     dummy = ListNode(0)
    #     tail = dummy
    #
    #     while not heap.empty():
    #         head = heap.get()[1]
    #         tail.next = head
    #         tail = tail.next
    #         if head.next is not None:
    #             heap.put((head.next.val, head.next))
    #
    #     return dummy.next

    # ######################## Merge Two By Two ######################## #
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

    def mergeKLists(self, lists):
        if lists is None or not lists:
            return None

        while len(lists) > 1:
            new_lists = []
            for i in xrange(0, len(lists)-1, 2):
                merged_list = self.merge(lists[i], lists[i+1])
                new_lists.append(merged_list)
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
            lists = new_lists

        return lists[0]


sol = Solution()
linked_lst = []
head1 = ListNode(1, ListNode(3, ListNode(5, ListNode(8))))
linked_lst.append(head1)
head2 = ListNode(0, ListNode(6, ListNode(10, ListNode(30))))
linked_lst.append(head2)
head3 = ListNode(4, ListNode(9, ListNode(23)))
linked_lst.append(head3)

print_list(sol.mergeKLists(linked_lst))
