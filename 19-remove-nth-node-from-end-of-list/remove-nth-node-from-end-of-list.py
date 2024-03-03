# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start, fast = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast and fast.next:
            start = start.next
            fast = fast.next
        start.next = start.next.next
        #print(start.val, fast.val)
        return head
        