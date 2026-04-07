class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for i in range(len(nums)):
            colors[nums[i]] += 1
        
        k = 0
        for i in range(3):
            for j in range(colors[i]):
                nums[k] = i
                k += 1