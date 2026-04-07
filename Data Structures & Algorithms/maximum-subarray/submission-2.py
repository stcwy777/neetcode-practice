class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # left = 0
        curSum, maxSum = 0, nums[0]
        
        for i in range(len(nums)):
            curSum += nums[i]

            if maxSum < curSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum
