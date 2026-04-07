class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        if nums_len <= 1:
            k = nums_len
        else:
            k = 1
            for i in range(1, nums_len):
                if nums[i] != nums[k-1]:
                    nums[k] = nums[i]
                    k += 1
        return k
