class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        l_sum = [0] * len(nums)

        if tot_sum == nums[0]:
            return 0
        for i in range(1, len(nums)):
            l_sum[i] = l_sum[i - 1] + nums[i - 1]
            if l_sum[i] == (tot_sum - nums[i] - l_sum[i]):
                return i
        return -1