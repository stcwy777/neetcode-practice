class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            newPerms = []
            dedup = set()
            for p in perms:
                for i in range(len(p) + 1):
                    newP = p.copy()
                    newP.insert(i, num)
                    if tuple(newP) not in dedup:
                        newPerms.append(newP)
                        dedup.add(tuple(newP))
            perms = newPerms
        return perms