# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        S = []
        def dfs(node: TreeNode) -> None:
            if not node:
                S.append('N')
                return
            
            S.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return ",".join(S)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        S = deque(data.split(','))

        def dfs() -> TreeNode:
            
            if S[0] == 'N':
                S.popleft()
                return None
            
            node = TreeNode(val=int(S.popleft()))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

        
