class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        new = 0
        
        while 1:
            while n:
                new += (n % 10) ** 2
                n = n // 10
            if new == 1:
                return True
            elif new in seen:
                return False
            else:
                seen.add(new)
                n = new
                new = 0
