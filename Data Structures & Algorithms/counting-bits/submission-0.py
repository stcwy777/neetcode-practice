class Solution:
    def countBits(self, n: int) -> List[int]:
        def findBits(n: int) -> int:
            counts = 0
            while n:
                if n & 1:
                    counts += 1
                n = n >> 1
            return counts
        
        rslt = [0] * (n + 1)
        for i in range(n + 1):
            rslt[i] = findBits(i)
        
        return rslt