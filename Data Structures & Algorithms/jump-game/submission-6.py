class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(0, n):              
            if max_reach >= i:
                max_reach = max(max_reach, nums[i] + i)
                if max_reach >= n - 1:
                    return True                
            else:
                return False
        return False

