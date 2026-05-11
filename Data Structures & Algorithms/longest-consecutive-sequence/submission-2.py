class UnionFind:
    def __init__(self):
        self.roots = {}

    def find(self, x: int) -> int:

        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x: int, y: int):
        if x not in self.roots or y not in self.roots:
            return
        root_x = self.find(x)
        root_y = self.find(y)
        self.roots[root_y] = root_x

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uf = UnionFind()
        longest = 1
        counts = {}
        for num in nums:
            if num in uf.roots:
                continue
            uf.roots[num] = num
            counts[num] = 0
            uf.union(num - 1, num)
            uf.union(num, num + 1)

        for num in uf.roots.keys():
            root = uf.find(num)
            counts[root] += 1
            longest = max(longest, counts[root])
        
        return longest