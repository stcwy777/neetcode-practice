class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        tot_wt = 0

        for R in range(1, len(height)):
            
            if R - L == 1:
                if height[L] < height[R]:
                    L = R
            elif R - L > 1:
                if height[R] >= height[L]:
                    water = sum([height[L] - height[i] for i in range(L + 1, R)])
                    tot_wt += water
                    L = R

        R = len(height) - 1
        boundary = L - 1
        for L in range(len(height) - 2, boundary, -1):
            
            if R - L == 1:
                if height[R] < height[L]:
                    R = L
            elif R - L > 1:
                if height[L] >= height[R]:
                    water = sum([height[R] - height[i] for i in range(R - 1, L, -1)])
                    tot_wt += water
                    R = L
        
        return tot_wt