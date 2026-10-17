class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        memo = {}

        def dfs(l: int, r: int) -> int:
            if r <= l + 1:
                return 0

            if (l, r) in memo:
                 return memo[(l, r)]
            ans = 0
            for k in range(l + 1, r):
                ans = max(ans, dfs(l, k) + dfs(k, r) + nums[l] * nums[r] * nums[k])

            memo[(l, r)] = ans
            return ans
        
        return dfs(0, n - 1)
            
