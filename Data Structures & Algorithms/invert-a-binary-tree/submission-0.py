# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node: TreeNode):

            if not node:
                return
            
            invert(node.left)
            invert(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp

            return
        
        invert(root)
        return root