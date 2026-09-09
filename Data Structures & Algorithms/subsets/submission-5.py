class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []
        
        def dfs(start: int) -> None:
            res.append(comb[:])
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                dfs(i + 1)
                comb.pop()
        
        dfs(0)

        return res