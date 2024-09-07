# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def track(node, start):
            if not start:
                return True
            if not node:
                return False
            if node.val != start.val:
                return False
            return track(node.left, start.next) or track(node.right, start.next)
        self.res = False
        def dfs(node):
            if not node:
                return
            if node.val == head.val:
                start = head
                self.res = self.res or  track(node, start)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
            

        