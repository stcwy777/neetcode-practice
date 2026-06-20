class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x: int, y: int) -> bool:
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return False
        
        if self.rank[par_x] < self.rank[par_y]:
            self.par[par_x] = par_y
        elif self.rank[par_x] > self.rank[par_y]:
            self.par[par_y] = par_x
        else:
            self.par[par_y] = par_x
            self.rank[par_x] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def mst(valid_edges: List[List[int]], pre_edge=None) -> int:
            uf = UnionFind(n)
            edge_heap = []

            for x, y, w in valid_edges:
                heapq.heappush(edge_heap, (w, x, y))

            cost = 0
            edge_count = 0
            
            if pre_edge:
                x, y, w = pre_edge
                uf.union(x, y)            
                cost += w
                edge_count += 1
            
            while edge_heap and edge_count < n - 1:
                w, x, y = heapq.heappop(edge_heap)

                if not uf.union(x, y):
                    continue
                
                cost += w
                edge_count += 1
            
            return cost if edge_count == n - 1 else - 1
    
        min_cost = mst(edges)
        rslts = [[], []]

        for i in range(len(edges)):
            new_edges = edges[:i] + edges[i+1:]
            new_edges.sort(key=lambda x: x[2])
            new_cost = mst(new_edges)

            if new_cost == -1 or new_cost > min_cost:
                rslts[0].append(i)
            elif mst(new_edges, pre_edge=edges[i]) == min_cost:
                rslts[1].append(i)
        
        return rslts
            