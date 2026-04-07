class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        idx = -1

        while lp <= rp:
            mp = lp + (rp - lp) // 2
            if nums[mp] == target:
                idx = mp
                break
            elif nums[mp] < target:
                lp = mp + 1
            else:
                rp = mp - 1
        
        return idx