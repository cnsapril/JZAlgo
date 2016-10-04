import Queue as Q
from ListNode import ListNode, print_list


linked_lst = []
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

linked_lst.append(node1)
linked_lst.append(node2)
linked_lst.append(node3)

q = Q.PriorityQueue()
for item in linked_lst:
    q.put((item.val, item))

while not q.empty():
    print q.get()[1].val
