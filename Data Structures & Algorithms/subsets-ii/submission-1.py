class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rslt = [[]]
        offset = 0
        nums.sort()
        for i in range(len(nums)):
            subset = []
            if i and nums[i] == nums[i - 1]:
                for j in range(offset, len(rslt)):
                    subset.append(rslt[j] + [nums[i]])
            else:
                for j in range(len(rslt)):
                    subset.append(rslt[j] + [nums[i]])
            
            offset = len(rslt)
            rslt.extend(subset)
        return rslt

