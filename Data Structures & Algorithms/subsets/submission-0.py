class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]

        for i in range(len(nums)):
            for j in range(len(sets)):
                tmp = sets[j].copy()
                sets[j].append(nums[i])
                sets.append(tmp)
        return sets