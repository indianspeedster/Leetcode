# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        nex = head.next
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        while nex:
            cur.next = ListNode(gcd(cur.val, nex.val))
            cur.next.next = nex
            cur = nex
            nex = nex.next
        return head


        