# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        startNode, endNode = None, None
        start = list1
        for i in range(a-1):
            start = start.next
        startNode = start
        start = list1
        for i in range(b):
            start = start.next
        endNode = start.next
        startNode.next = list2
        start = list2
        while start.next:
            start = start.next
        start.next = endNode
        return list1
        