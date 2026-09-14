class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # x = 2 ** (len(nums) + 1) - 1

        # for num in nums:
        #     x = x >> num
        
        # return x
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
