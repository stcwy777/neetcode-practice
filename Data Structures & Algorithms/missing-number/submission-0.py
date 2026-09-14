class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # x = 2 ** (len(nums) + 1) - 1

        # for num in nums:
        #     x = x >> num
        
        # return x
        return sum(range(len(nums) + 1)) - sum(nums)