class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        h = dummy
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s//10
            value = s%10
            h.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            h = h.next
        while l1:
            s = l1.val + carry
            carry = s//10
            value = s%10
            h.next = ListNode(value)
            l1 = l1.next
            h = h.next
        while l2:
            s = l2.val + carry
            carry = s//10
            value = s%10
            h.next = ListNode(value)
            l2 = l2.next
            h = h.next
        if carry != 0:
            h.next = ListNode(carry)
        return dummy.next
        