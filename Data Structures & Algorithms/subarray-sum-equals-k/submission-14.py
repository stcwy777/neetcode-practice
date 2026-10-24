from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        sumHash = defaultdict(int)
        sumHash[0] = 1
        print(sumHash)
        for s in preSum[1:]:
            res += sumHash[s - k]
            sumHash[s] += 1
        return res
