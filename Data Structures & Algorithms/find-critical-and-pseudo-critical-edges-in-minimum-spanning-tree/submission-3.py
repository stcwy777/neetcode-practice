class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[px] > self.rank[py]:
            self.par[py] = px
        else:
            self.par[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda x: x[2])

        def mst(block=None, pre=None):
            uf = UnionFind(n)
            cost = 0
            count = 0

            if pre is not None:
                x, y, w, _ = edges[pre]
                if uf.union(x, y):
                    cost += w
                    count += 1

            for i, (x, y, w, _) in enumerate(edges):
                if i == block:
                    continue
                if uf.union(x, y):
                    cost += w
                    count += 1
                if count == n - 1:
                    break

            return cost if count == n - 1 else float('inf')

        min_cost = mst()
        critical = []
        pseudo = []

        for i in range(len(edges)):
            if mst(block=i) > min_cost:
                critical.append(edges[i][3])
            elif mst(pre=i) == min_cost:
                pseudo.append(edges[i][3])

        return [critical, pseudo]