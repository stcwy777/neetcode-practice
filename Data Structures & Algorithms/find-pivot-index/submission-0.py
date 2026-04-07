class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = [0] * len(nums)
        r_sum = [0] * len(nums)

        for i in range(1, len(nums)):
            l_sum[i] = l_sum[i - 1] + nums[i - 1]
            r_sum[i] = r_sum[i - 1] + nums[len(nums) - i]
        
        for i in range(len(nums)):
            if l_sum[i] == r_sum[len(nums) - i - 1]:
                return i
        return -1