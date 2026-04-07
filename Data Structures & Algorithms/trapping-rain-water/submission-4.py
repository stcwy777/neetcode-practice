class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        max_l = [0] * len(height)
        max_r = [0] * len(height)

        for i in range(1, len(height)):
            max_l[i] = max(height[i - 1], max_l[i - 1])
            max_r[len(height) - 1 - i] = max(max_r[len(height) - i], height[len(height) - i])
        tot_water = 0

        for i in range(1, len(height) - 1):
            tot_water += max(min(max_l[i], max_r[i]) - height[i], 0)
        return tot_water