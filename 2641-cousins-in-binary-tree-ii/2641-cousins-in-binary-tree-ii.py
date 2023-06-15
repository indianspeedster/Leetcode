# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        st = [node]
        while st:
            k = []
            s = 0
            for i in st:
                if i.left:
                    s += i.left.val
                if i.right:
                    s += i.right.val
            for i in st:
                node_sum = 0
                if i.left:
                    node_sum += i.left.val
                if i.right:
                    node_sum += i.right.val
                if i.left:
                    i.left.val = s-node_sum
                    k.append(i.left)
                if i.right:
                    i.right.val = s-node_sum
                    k.append(i.right)
            st = k
        root.val = 0
        return root
                    
                
                
                
        