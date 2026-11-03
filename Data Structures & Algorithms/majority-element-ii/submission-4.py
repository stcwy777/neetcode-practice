class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # at most 2 
        cand1, cand2 = None, None
        freq1, freq2 = 0, 0
        n = len(nums)
        bar = n // 3

        for num in nums:
            if num == cand1:
                freq1 += 1
            elif num == cand2:
                freq2 += 1
            elif freq1 == 0:
                cand1, freq1 = num, 1
            elif freq2 == 0:
                cand2, freq2 = num, 1
            else:
                freq1 -= 1
                freq2 -= 1
        
        res = []
        for num in (cand1, cand2):
            if num != None and nums.count(num) > bar:
                res.append(num)

        return res