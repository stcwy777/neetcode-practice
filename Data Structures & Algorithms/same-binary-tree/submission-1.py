# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pS = []
        qS = []

        def dfs(node: TreeNode, s: list) -> None:

            if not node:
                s.append('N')
                return

            s.append(str(node.val))
            dfs(node.left, s)
            dfs(node.right,s)
            
            return
        
        dfs(p, pS)
        dfs(q, qS)

        print(pS, qS)
        # if ''.join(pS) == ''.join(qS):
        if pS == qS:
            return True
        else:
            return False