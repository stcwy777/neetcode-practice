class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], 
                        dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    )
                    
        return dp[0][n - 1]