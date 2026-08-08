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

        def preOrder(node: TreeNode) -> None:
            if not node:
                S.append("N")
                return

            S.append(str(node.val))

            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)

        return ' '.join(S)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        vals = data.split()
        
        def dfs():
            if vals[0] == "N":
                vals.pop(0)
                return None

            node = TreeNode(int(vals.pop(0)))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


