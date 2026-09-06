class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [nums[0]] * n
        min_dp = [nums[0]] * n
        res = max_dp[0]

        for i in range(1, n):
            max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])
            min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])

            res = max(res, max_dp[i])

        return res