class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        inc = 1
        i = len(digits) - 1
        res = digits[:]
        while inc and i >= 0:
            res[i] += inc
            inc = res[i] // 10
            res[i] %= 10
            i -= 1
        
        if inc:
            res = [1] + res
        return res
