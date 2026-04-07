# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Delete logic: 
        if root is None:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                del root
                return None
            elif not root.right:
                node = root.left
                del root
                return node
            else:
                node = root.right
                while node.left:
                    node = node.left

                node.left = root.left
                res = root.right
                del root
                return res
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
                
                
                