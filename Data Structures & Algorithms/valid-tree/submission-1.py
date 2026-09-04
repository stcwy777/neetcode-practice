class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1            

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) < n - 1:
            return False
        uf = UnionFind(n)

        for edge in edges:
            x, y = (edge[0], edge[1]) if edge[0] < edge[1] else (edge[1], edge[0])

            if not uf.union(x, y):
                return False
        
        return True