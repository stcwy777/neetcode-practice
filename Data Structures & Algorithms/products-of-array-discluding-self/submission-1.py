class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rslt = [1] * len(nums)

        for i in range(1, len(nums)):
            rslt[i] = rslt[i - 1] * nums[i - 1]
        
        r = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            r[i] = r[i + 1] * nums[i+1]

            rslt[i] *= r[i]
        
        return rslt