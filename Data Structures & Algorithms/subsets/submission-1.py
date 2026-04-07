class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rslt = [[]]
        for num in nums:
            for i in range(len(rslt)):
                new = rslt[i] + [num]
                rslt.append(new)
        return rslt