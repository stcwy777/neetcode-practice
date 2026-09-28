class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reach = 0
        current_reach = 0
        n = len(nums)

        for i in range(n - 1):
            max_reach = max(max_reach, nums[i] + i)

            if i == current_reach:
                jumps += 1
                current_reach = max_reach
        
        return jumps