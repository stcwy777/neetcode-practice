class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        area = min(heights[L], heights[R]) * (R - L)

        while L <= R:
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
            area = max(area, min(heights[L], heights[R]) * (R - L))
        
        return area