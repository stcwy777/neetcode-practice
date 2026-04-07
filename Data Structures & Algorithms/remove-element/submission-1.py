class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1
                j -= 1
        return i

