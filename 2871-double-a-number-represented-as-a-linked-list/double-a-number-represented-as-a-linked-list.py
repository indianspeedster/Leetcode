# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        start = head
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        start = prev
        carry = 0
        while start.next:
            val = (start.val * 2 + carry) % 10
            carry = (start.val *2) // 10
            start.val = val
            start = start.next
        val = (start.val * 2 + carry) % 10
        carry = (start.val *2) // 10
        start.val = val
        if carry != 0:
            start.next = ListNode(carry)


        start =  prev
        prev = None
        while start:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        return prev
