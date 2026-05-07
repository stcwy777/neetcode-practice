class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [0] * n
    
    def find(self, x: int) -> int:
        parent = self.parents[x]
        while self.parents[x] != x:
            x = self.parents[x]
        self.parents[x] = x
        return x

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[x] > self.rank[y]:
                self.parents[root_y] = root_x
            elif self.rank[x] < self.rank[y]:
                self.parents[root_x] = root_y
            else:
                self.parents[root_y] = root_x
                self.rank[x] += 1
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_idx = {}
        uf = UnionFind(len(accounts))

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in email_idx:
                    uf.union(email_idx[email], i)
                else:
                    email_idx[email] = i
        dedup_acc = {}

        for i in range(len(accounts)):
            root_i = uf.find(i)
            if root_i not in dedup_acc:
                dedup_acc[root_i] = set()
            for email in accounts[i][1:]:
                dedup_acc[root_i].add(email)
        
        rslt = []
        for root_i, emails in dedup_acc.items():
            rslt.append([accounts[root_i][0]] + list(emails))
        return rslt

