# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list = defaultdict(list)
        self.start_node = 0

        def dfs(node):
            if not node:
                return
            if node.left:
                adj_list[node].append(node.left)
                adj_list[node.left].append(node)
            if node.right:
                adj_list[node].append(node.right)
                adj_list[node.right].append(node)
            if node.val == start:
                self.start_node = node
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        st = [self.start_node]
        cnt = -1
        vis = set()
        
        
        while st:
            cur_list = []
            for node in st:
                vis.add(node)
                for leaf in adj_list[node]:
                    if leaf not in vis:
                        cur_list.append(leaf)
                        
            cnt += 1
            st = cur_list
        return cnt

                



        
        