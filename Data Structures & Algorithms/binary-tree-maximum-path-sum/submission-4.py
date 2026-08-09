# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node: TreeNode) -> int:
            nonlocal maxSum
            if not node:
                return 0
            
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            pathSum = node.val + leftSum + rightSum
            gain = node.val + max(leftSum, rightSum)
            maxSum = max(maxSum, max(pathSum, gain))
            
            return gain

        dfs(root)

        return maxSum