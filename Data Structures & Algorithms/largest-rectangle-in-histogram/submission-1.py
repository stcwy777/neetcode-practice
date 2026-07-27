class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        area = 0
        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                cur = stack.pop()
                left = stack[-1] + 1
                right = i - 1
                width = i - 1 - stack[-1]
                area = max(area, heights[cur] * width)

            stack.append(i)
        return area