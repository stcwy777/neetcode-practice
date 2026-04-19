class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]
            # sumHash[preSum[i+1]] = sumHash.get(preSum[i + 1], 0) + 1
        
        sumHash = {0: 1}
        total = 0
        for s in preSum[1:]:
            total += sumHash.get(s - k, 0)
            sumHash[s] = sumHash.get(s, 0) + 1

        return total