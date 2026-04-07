class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        max_sums = [nums[0]] * len(nums)
        min_sums = [nums[0]] * len(nums)
        total, max_val, min_val = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            total += nums[i]

            max_sums[i] = max(max_sums[i - 1] + nums[i], nums[i])
            max_val = max(max_val, max_sums[i])
            
            min_sums[i] = min(min_sums[i - 1] + nums[i], nums[i])
            min_val = min(min_val, min_sums[i])

        if min_val != total:
            return max(max_val, total - min_val)
        else:
            return max(nums)