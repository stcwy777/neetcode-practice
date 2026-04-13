class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        cur_max, cur_min = nums[0], nums[0]
        overall_max, overall_min = nums[0], nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            
            total += nums[i]
            
            # max ending at i
            cur_max = max(nums[i], cur_max + nums[i])
            overall_max = max(cur_max, overall_max)

            # min value at i
            cur_min = min(nums[i], cur_min + nums[i])
            overall_min = min(overall_min, cur_min)

        if overall_min == total:
            return max(nums)
        return max(overall_max, total - overall_min)
            