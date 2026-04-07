# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Helper
        def inOrderTraverse(root: Optional[TreeNode]) -> list:

            if not root:
                return []
            stack = []

            stack.extend(inOrderTraverse(root.left))
            stack.append(root.val)
            stack.extend(inOrderTraverse(root.right))

            return stack

        stack = inOrderTraverse(root)
        return stack[k-1]