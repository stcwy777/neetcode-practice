class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        rslt = []

        def helper(start: int, comb: List[int]) -> None:
            
            for i in range(start, n + 1):
                new_comb = comb + [i]
                if len(new_comb) == k:
                    rslt.append(new_comb)
                else:
                    helper(i + 1, new_comb)
            return
        helper(1, [])
        return rslt