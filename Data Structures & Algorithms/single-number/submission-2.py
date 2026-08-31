class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for n in nums:
            if n > 0:
                x = x ^ (1 << n)
            else:
                y = y ^ (1 << -n)

        power = 0
        z = max(x, y)
        while z > 1:
            z >>= 1  
            power += 1
        if x:
            return power
        else:
            return -power