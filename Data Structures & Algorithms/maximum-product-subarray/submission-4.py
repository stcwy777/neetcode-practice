class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = nums[0]
        min_dp= nums[0]
        res = max_dp

        for i in range(1, n):
            max_dp_n = max(nums[i], nums[i] * max_dp, nums[i] * min_dp)
            min_dp_n = min(nums[i], nums[i] * max_dp, nums[i] * min_dp)

            res = max(res, max_dp_n)
            max_dp = max_dp_n
            min_dp = min_dp_n


        return res