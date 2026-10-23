class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = nums[:]
        min_dp = nums[:]
        
        for i in range(1, n):
            max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])


        return max(max_dp)
