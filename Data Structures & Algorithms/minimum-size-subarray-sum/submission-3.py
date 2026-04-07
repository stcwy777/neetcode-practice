class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R, length = 0, 0, len(nums) + 1
        cur_sum = nums[0]

        while L <= R and R < len(nums):          
            if cur_sum >= target:
                length = min(length, R - L + 1)

                if length == 1:
                    break
                cur_sum -= nums[L]
                L += 1                
            else:
                R += 1
                if R < len(nums):
                    cur_sum += nums[R]  

        if length == len(nums) + 1:
            length = 0
        return length