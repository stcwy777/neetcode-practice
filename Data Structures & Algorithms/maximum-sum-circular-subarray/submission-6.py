class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        cur_max = nums[0]
        cur_min = nums[0]
        total, max_val, min_val = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            total += nums[i]

            cur_max = max(cur_max + nums[i], nums[i])
            max_val = max(max_val, cur_max)
            
            cur_min = min(cur_min + nums[i], nums[i])
            min_val = min(min_val, cur_min)

        if min_val != total:
            return max(max_val, total - min_val)
        else:
            return max(nums)