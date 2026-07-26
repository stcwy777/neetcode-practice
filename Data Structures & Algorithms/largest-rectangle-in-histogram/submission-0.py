class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()
                area = max(area, heights[idx] * (i - 1 - stack[-1]))

            stack.append(i)

        return area