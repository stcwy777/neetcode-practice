class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        freq = {}
        minV = float('INF')
        maxV = float('-INF')

        for num in nums:
            if freq.get(num, 0):
                return False
            freq[num] = 1
            maxV = max(num, maxV)
            minV = min(num, minV)
        if (maxV - minV + 1) == len(nums):
            return True
        else:
            return False
