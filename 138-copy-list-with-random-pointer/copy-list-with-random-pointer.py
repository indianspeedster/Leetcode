"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashMap = {}
        cur = head
        while cur:
            hashMap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            node = hashMap[cur]
            if cur.next:
                node.next = hashMap[cur.next]
            if cur.random:
                node.random = hashMap[cur.random]
            cur = cur.next
        return hashMap[head]

        