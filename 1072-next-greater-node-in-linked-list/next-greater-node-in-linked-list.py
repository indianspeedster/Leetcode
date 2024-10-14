# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        start = head
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        start = prev
        ans = []
        st = []
        while start:
            if not st:
                st.append(start.val)
                start = start.next
                ans.append(0)
                continue
            while st and start.val >= st[-1]:
                st.pop()
            if not st:
                ans.append(0)
            else:
                ans.append(st[-1])
            st.append(start.val)
            start = start.next
        return ans[::-1]
        