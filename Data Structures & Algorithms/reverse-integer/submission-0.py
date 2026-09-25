class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1

        res = 0
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        
        res *= sign

        if res >= 2 ** 31 or res < -2**31:
            return 0
        return res