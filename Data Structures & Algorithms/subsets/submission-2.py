class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rslt = [[]]

        for i in range(len(nums)):
            new_s = []
            for s in rslt:
                new_s.append(s + [nums[i]])
            rslt.extend(new_s)
        return rslt