class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        the_sum = sum(nums)

        if the_sum % 2:
            return False
        
        bag = the_sum // 2
        N = len(nums)
        dp = [[False] * (bag + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(1, N + 1):
            for j in range(bag + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[N][bag]
