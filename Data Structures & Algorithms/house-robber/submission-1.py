class Solution:
    def rob(self, nums: List[int]) -> int:
        values = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        values[0] = nums[0]
        values[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            values[i] = max(values[i-1], values[i-2] + nums[i])
        return values[len(nums)-1]