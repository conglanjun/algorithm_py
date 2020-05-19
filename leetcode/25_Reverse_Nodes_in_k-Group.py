"""
1->2->3->4->5

loop 1:
p = 1
p->None
e->p

e->p->None
e->1->2
p = 2

loop 2:
e->2->1
p=3

loop 3:
e->3->2->1
p=4

e=s=1

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head, k):
        p = head
        e = r = ListNode(None)
        n = 0
        while head:
            head = head.next
            n += 1

        for i in range(n // k):
            s = p
            count = 0
            while count < k:
                count += 1
                p.next, e.next, p = e.next, p, p.next
            e = s
        e.next = p
        return r.next

