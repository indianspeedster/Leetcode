# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set(nums)
        start = ListNode(0)
        start.next = head
        toReturn = start
        while start and start.next:
            while start.next and start.next.val in hashSet:
                start.next = start.next.next
            start = start.next
        return toReturn.next

        