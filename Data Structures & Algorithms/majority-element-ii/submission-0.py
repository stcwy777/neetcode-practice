from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        cut = n // 3 + 1

        freq = Counter(nums)

        for k, v in freq.items():
            if v >= cut:
                res.append(k)
        return res
