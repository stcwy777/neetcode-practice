# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        minBoundary = float('-INF')
        maxBoundary = float('INF')

        def dfs(node: TreeNode, minB: int, maxB: int) -> bool:

            if not node:
                return True
            
            if node.val <= minB or node.val >= maxB:
                return False

            return dfs(node.left, minB, node.val) and dfs(node.right, node.val, maxB)

        return dfs(root, float('-INF'), float('INF'))