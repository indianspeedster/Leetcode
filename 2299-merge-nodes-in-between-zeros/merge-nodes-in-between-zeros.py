# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        start = dummy
        first = head
        curr = 0
        while first:
            if first.val == 0 and curr != 0:
                node = ListNode(val=curr)
                start.next = node
                start = start.next
                first = first.next
                curr = 0
            else:
                curr += first.val
                first = first.next
        return dummy.next

        