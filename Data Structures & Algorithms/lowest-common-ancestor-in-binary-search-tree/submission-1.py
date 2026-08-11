# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.left == q or p.right == q:
            return p
        if q.left == p or q.right == p:
            return q
        def preorder(node: TreeNode, val: int, path: list) -> bool:
            
            if not node:
                return False

            if node.val == val:
                path.append(node)
                return True
            
            path.append(node)

            if node.val > val:
                return preorder(node.left, val, path)
            else:
                return preorder(node.right, val, path)

        sp = []
        sq = []

        if not preorder(root, p.val, sp) or not preorder(root, q.val, sq):
            return None

        for s in reversed(sp):
            if s in sq:
                return s