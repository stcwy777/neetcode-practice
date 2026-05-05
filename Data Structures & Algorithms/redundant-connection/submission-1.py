class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[x] < self.rank[y]:
                self.parent[root_x] = root_y
            elif self.rank[x] > self.rank[y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[x] += 1
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for x, y in edges:
            if uf.find(x) == uf.find(y):
                return [x, y]
            else:
                uf.union(x, y)
        