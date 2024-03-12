class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        start = dummyNode

        while start:
            end = start.next
            prefixSum = 0
            while end:
                prefixSum += end.val
                if prefixSum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return dummyNode.next