class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = 0
        
        cur_max = 0
        max_sum = nums[0]
        
        cur_min = 0
        min_sum = nums[0]
        
        for x in nums:
            total += x
            
            # Kadane for max subarray sum
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            
            # Kadane for min subarray sum
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
        
        # If all numbers are negative, max_sum is the answer
        if max_sum < 0:
            return max_sum
        
        # Otherwise, max of non-wrap and wrap
        return max(max_sum, total - min_sum)
