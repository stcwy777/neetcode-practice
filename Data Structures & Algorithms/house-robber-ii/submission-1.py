class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def help(N: List[int]) -> int:
            n = len(N)
            dp = [0] * (n + 1)
            dp[1] = N[0]
    
            for i in range(2, n + 1):
                dp[i] = max(N[i - 1] + dp[i - 2], dp[i - 1])
            
            return dp[n]
        if len(nums) == 1:
            return nums[0]
        return max(help(nums[1:]), help(nums[:-1]))