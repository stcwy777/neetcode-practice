class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)
        
        k_valid = 1
        while k_min <= k_max:
            k_mid = k_min + (k_max - k_min) // 2
            h_trial = sum([math.ceil(x / k_mid) for x in piles])

            if h_trial > h:
                k_min = k_mid + 1
            else:
                k_max = k_mid - 1
                k_valid = k_mid

        return k_valid
