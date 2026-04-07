class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = [0] * (len(nums) + 1)
        rslt = 0
        sum_hash = {0: 1}   
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            target = prefix_sum[i + 1] - k
            rslt += sum_hash.get(target, 0)
            sum_hash[prefix_sum[i + 1]] = sum_hash.get(prefix_sum[i + 1], 0) + 1
        
        return rslt