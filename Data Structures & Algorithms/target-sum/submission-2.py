class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i: int, res: int) -> int:
            if i == len(nums):
                if res == 0:
                    return 1
                else:
                    return 0
            else:
                return dfs(i + 1, res - nums[i]) + dfs(i + 1, res + nums[i])
        
        return dfs(0, target)
            
