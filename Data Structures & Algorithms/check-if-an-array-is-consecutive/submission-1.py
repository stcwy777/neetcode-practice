class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        n = len(nums)

        if max(nums) - min(nums) + 1 == n and len(set(nums)) == n:
            return True
        return False