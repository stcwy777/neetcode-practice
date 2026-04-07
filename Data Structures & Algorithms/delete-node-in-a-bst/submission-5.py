# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        ancestor = None
        ancestor_dir = None
        node = root
        while node:
            # Found node-to-del
            if key == node.val:
                # if node-to-del has right branches
                if node.right:
                    ancestor = node
                    probe = node.right
                    ancestor_dir = 1

                    while probe.left:
                        ancestor = probe
                        probe = probe.left
                        ancestor_dir = 0

                    node.val = probe.val
                    if ancestor_dir == 0:
                        ancestor.left = probe.right
                    else:
                        ancestor.right = probe.right
                    del probe
                # if node-to-del has only left branches or no branch
                # not deleting root node
                elif ancestor:
                    if ancestor_dir == 0:
                        ancestor.left = node.left
                    else:
                        ancestor.right = node.left
                    del node
                # deleting root node
                else:
                    root = root.left
                    del node
                break
            elif key < node.val:
                ancestor = node
                ancestor_dir = 0
                node = node.left
            else:
                ancestor = node                
                ancestor_dir = 1
                node = node.right
        return root
