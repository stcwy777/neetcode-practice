# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def value(node: TreeNode) -> int:
            nonlocal maxSum
            if not node:
                return 0
            
            left = max(value(node.left), 0)
            right = max(value(node.right), 0)

            path = node.val + left + right
            gain = node.val + max(left, right)
              
            maxSum = max(maxSum,  max(gain, path))
            
            return gain
        
        value(root)
        return maxSum
