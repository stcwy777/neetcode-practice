# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Helper
        def inOrderTraverse(root: Optional[TreeNode], k: int) -> list:

            if not root or k <= 0:
                return []
            stack = []

            stack.extend(inOrderTraverse(root.left, k))
            stack.append(root.val)
            k -= 1
            stack.extend(inOrderTraverse(root.right, k))

            return stack

        stack = inOrderTraverse(root, k)
        return stack[k-1]