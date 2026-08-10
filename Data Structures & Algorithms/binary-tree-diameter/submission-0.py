# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = float('-inf')

        def dfs(node: TreeNode) -> int:
            nonlocal maxD

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            gain = max(left, right) + 1

            maxD = max(maxD, left + right)
            return gain

        dfs(root)

        return maxD