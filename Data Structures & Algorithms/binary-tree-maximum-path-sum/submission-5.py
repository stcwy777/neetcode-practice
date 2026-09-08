# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-INF')

        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, node.val + max(0, left) + max(0, right))
            # print(res)
            return node.val + max(max(0, left), max(0, right))

        v = dfs(root)
        return max(res, v)