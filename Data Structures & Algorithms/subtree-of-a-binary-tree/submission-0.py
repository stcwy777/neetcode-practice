# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node: TreeNode) -> str:
            if not node:
                return 'N'

            return str(node.val) + dfs(node.left) + dfs(node.right)
        
        if dfs(subRoot) in dfs(root):
            return True
        else:
            return False
