# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            start = node
            while start:
                temp = start.next
                start.next = prev
                prev = start
                start = temp
            return prev
        storeList = []
        node = head
        while node:
            start = node
            end = False
            
            for i in range(k-1):
                print(node.val)
                if not node.next:
                    end = True
                    node = node.next
                    break
                else:
                    node = node.next
            print(end)
            if end:
                print("true")
                reverseHead = start
                start = None

            else:
                cur = node
                node = node.next if node else None
                if cur:
                    cur.next = None
                reverseHead = reverse(start)
            storeList.append((reverseHead, start))
        returnNode = storeList[0][0]

        for i, (start, end) in enumerate(storeList):
            if i == len(storeList) - 1:
                break
            end.next = storeList[i+1][0]
        return returnNode
                
                        