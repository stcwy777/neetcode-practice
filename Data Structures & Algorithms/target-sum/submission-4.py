class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2:
            return 0
        
        p = (total_sum + target) // 2
        dp = [[0] * (p + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(p + 1):
                dp[i][j] = dp[i - 1][j]

                if j >= nums[i-1]:
                    dp[i][j] += dp[i - 1][j-nums[i-1]]
        
        return dp[len(nums)][p]