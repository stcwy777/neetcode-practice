class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left = 0
        maxSum = nums[0]
        
        for right in range(1, len(nums) + 1):
            curSum = sum(nums[left:right])

            if maxSum < curSum:
                maxSum = curSum
            if curSum < 0:
                left = right
        return maxSum