"""
1->2->3->4
s=1
f=2

s=2
f=4

s=3
f=3

"""

class Solution:
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False