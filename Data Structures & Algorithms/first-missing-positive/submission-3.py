class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                print(nums[i], nums[nums[i] - 1], nums[nums[i] - 1], nums[i])
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
            else:
                i += 1

        print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1