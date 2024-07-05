# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(node):
            if node and node.next and node.next.next:
                if node.next.val > node.val and node.next.val > node.next.next.val:
                    return True
                if node.next.val < node.val and node.next.val < node.next.next.val:
                    return True
                else:
                    return False
            else:
                return False
        critical = False
        arr = []
        cur = 0
        start = head
        while start:
            if isCritical(start):
                arr.append(cur + 1)
            start = start.next
            cur += 1
        if len(arr) < 2:
            return [-1, -1]
        slow, fast = 0, 1
        maxi = arr[-1] - arr[0]
        mini = float("inf")
        while fast < len(arr):
            mini = min(mini, arr[fast] - arr[slow])
            fast += 1
            slow += 1
        return [mini, maxi]

        
    
    

                

