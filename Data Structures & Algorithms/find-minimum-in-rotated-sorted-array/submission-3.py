class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:

            if nums[l] < nums[r]:
                return nums[l]
            else:
                m = (r - l) // 2 + l
                if nums[l] > nums[m]:
                    r = m
                else:
                    l = m + 1

        return nums[l]