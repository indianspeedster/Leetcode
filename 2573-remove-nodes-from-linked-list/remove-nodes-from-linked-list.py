# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeVals = []
        start = head
        while start:
            if not nodeVals:
                nodeVals.append(start.val)
            else:
                while nodeVals and nodeVals[-1] < start.val:
                    nodeVals.pop()
                nodeVals.append(start.val)
            start = start.next
        dummyNode = ListNode(val = nodeVals[0])
        head = dummyNode
        for node in nodeVals[1:]:
            head.next = ListNode(val = node)
            head = head.next
        return dummyNode

        