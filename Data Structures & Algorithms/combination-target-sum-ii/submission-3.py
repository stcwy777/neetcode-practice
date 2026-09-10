class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        comb = []
        res = []

        def dfs(start: int, tar: int) -> None:
            if tar == 0:
                res.append(comb[:])
                return 
            if  tar < 0:
                return
            
            for i in range(start, n):

                if candidates[i] > tar:
                    break
                elif i > start and candidates[i] == candidates[i - 1]:
                    continue    
                comb.append(candidates[i])
                dfs(i + 1, tar - candidates[i])
                comb.pop()
            return
        
        dfs(0, target)

        return res