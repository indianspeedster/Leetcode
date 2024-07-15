# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict = {}
        for parent, child, side in descriptions:
            if parent not in treeDict:
                treeDict[parent] = (TreeNode(parent), -1)
            if child not in treeDict:
                treeDict[child] = (TreeNode(child), -1)
            if side:
                treeDict[parent][0].left =   treeDict[child][0]
                node, parent =   treeDict[child] 
                treeDict[child]  = (node, parent+1)
            else:
                treeDict[parent][0].right =   treeDict[child][0]
                node, parent =   treeDict[child] 
                treeDict[child]  = (node, parent+1)
        for node, parrent in treeDict.values():
            if parrent ==-1:
                return node
