class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        # output = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        pre = 1
        for i in range(len(nums) - 2, -1, -1):
            cur = pre * nums[i + 1]
            left[i] = left[i] * cur
            pre = cur
        return left