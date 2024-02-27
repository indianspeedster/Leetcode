# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        p2 = p1.next
        prev = None
        cur = p2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        p1.next = prev
        p1 = head
        maxi = 0
        while prev :
            maxi = max(maxi, prev.val + p1.val)
            p1 = p1.next
            prev = prev.next
        return maxi

        