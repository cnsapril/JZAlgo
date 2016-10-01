# coding=utf-8
from ListNode import ListNode, print_list
from Queue import PriorityQueue


# 1. 反转链表
def reverse(head):
    if head is None or head.next is None:
        return head

    prev, curt = None, head

    while curt is not None:
        temp = curt.next
        curt.next = prev
        prev = curt
        curt = temp

    return prev


# 2. 反转链表的m-n个node
def find_k_th(head, k):
    for i in range(k):
        if head is None:
            return None
        head = head.next

    return head


def reverse_between(head, m, n):
    if head is None or head.next is None:
        return head

    dummy = ListNode(0, head)

    # 特别注意此处find_k_th的第一个参数为dummy，而不是head。head应该为1st node，所以head = find_k_th(dummy, 1)。
    pre_m = find_k_th(dummy, m-1)
    m_th = pre_m.next
    n_th = find_k_th(dummy, n)
    post_n = n_th.next

    n_th.next = None
    reverse(m_th)

    pre_m.next = n_th
    m_th.next = post_n

    return dummy.next


# 3. 归并链表
def merge(list1, list2):
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


# 4. 找中点
def find_middle(head):
    if head is None:
        return head

    slow, fast = head, head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow


# 5. 增加节点
def add_node(head, node):
    if head is None:
        return node

    curt = head
    while curt.next is not None:
        curt = curt.next

    curt.next = node
    return head


# 6. 插入节点
def insert_node(head, node, k):
    if head is None:
        return head

    dummy = ListNode(0, head)
    pre_k = find_k_th(dummy, k-1)
    k_th = pre_k.next
    pre_k.next = node

    node_tail = node
    while node_tail.next is not None:
        node_tail = node_tail.next

    node_tail.next = k_th

    return dummy.next


# 7. 删除节点
def delete_node(head, k):
    if head is None:
        return None

    dummy = ListNode(0, head)
    pre_k = find_k_th(dummy, k-1)
    post_k = pre_k.next.next

    pre_k.next = post_k

    return dummy.next


# 8. 链表上的归并排序
def merge_sort(head):
    if head is None or head.next is None:
        return head

    mid = find_middle(head)
    right = merge_sort(mid.next)
    mid.next = None
    left = merge_sort(head)

    return merge(left, right)


# 9. 计算链表长度
def find_length(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length


# 10. 使用归并排序归并K个排序链表
def merge_helper(lists, start, end):
    if start == end:
        return lists[start]

    mid = start + (end - start) / 2
    left = merge_helper(lists, 0, mid)
    right = merge_helper(lists, mid+1, end)

    return merge(left, right)


def merge_k_lists(lists):
    if lists is None or not lists:
        return None

    return merge_helper(lists, 0, len(lists)-1)


# 11. 使用堆排序归并K个排序链表
def heap_merge_k_lists(lists):
    if lists is None or not lists:
        return None

    heap = PriorityQueue()
    for node in lists:
        if node is not None:
            heap.put((node.val, node))

    dummy = ListNode(0)
    tail = dummy

    while not heap.empty():
        head = heap.get()[1]
        tail.next = head
        tail = tail.next
        if head.next is not None:
            heap.put((head.next.val, head.next))

    return dummy.next


# 12. 两两归并N个排序链表
def two_by_two_merge_k_lists(lists):
    if lists is None or not lists:
        return None

    while len(lists) > 1:
        new_lists = []
        for i in xrange(0, len(lists)-1, 2):
            merged_list = merge(lists[i], lists[i+1])
            new_lists.append(merged_list)
        if len(lists) % 2 == 1:
            new_lists.append(lists[-1])
        lists = new_lists

    return lists[0]


print "\n1. Reverse Test"
print_list(reverse(ListNode(1, ListNode(2, ListNode(3)))))
print "\n2. Reverse m-n test"
print_list(reverse_between(ListNode(1, ListNode(2, ListNode(3))), 1, 2))
print "\n3. Merge Test"
print_list(merge(ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6)))))
print "\n4. Find Middle Test"
print find_middle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).val
print "\n5. Add Node Test"
print_list(add_node(ListNode(1, ListNode(3)), ListNode(2, ListNode(5))))
print "\n6. Insert Node Test"
print_list(insert_node(ListNode(1, ListNode(3)), ListNode(2, ListNode(5)), 1))
print "\n7. Delete Node Test"
print_list(delete_node(ListNode(1, ListNode(2, ListNode(3))), 3))
print "\n8. Merge Sort Test"
print_list(merge_sort(ListNode(3, ListNode(5, ListNode(1, ListNode(4, ListNode(2)))))))
print "\n10. Merge K Lists Test"
lists = [ListNode(1, ListNode(3)), ListNode(2, ListNode(5)), ListNode(19)]
print_list(merge_k_lists(lists))
print "\n11. Heap Merge K Lists Test"
lists1 = [ListNode(1, ListNode(3)), ListNode(2, ListNode(5)), ListNode(19)]
print_list(heap_merge_k_lists(lists1))
print "\n12. Two By Two Merge K Lists Test"
lists2 = [ListNode(1, ListNode(3)), ListNode(2, ListNode(5)), ListNode(19)]
print_list(two_by_two_merge_k_lists(lists2))





