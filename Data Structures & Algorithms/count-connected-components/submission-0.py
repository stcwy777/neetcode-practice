class UnionFind:
    def __init__(self, n: int):
        self.roots = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        
        return self.roots[x]
    
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        rank_x = self.rank[x]
        rank_y = self.rank[y]

        if root_x != root_y:
            if rank_x > rank_y:
                self.roots[root_y] = root_x
            elif rank_x < rank_y:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x
                self.rank[x] += 1
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for i, j in edges:
            uf.union(i, j)
        
        count = 0

        for i in range(n):
            if i == uf.find(i):
                count += 1
        return count