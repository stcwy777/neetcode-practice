class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        rslt = []

        def explore(path: List[int], tar: int, idx: int) -> None:

            if tar == 0:
                rslt.append(path.copy())
                return
            elif tar < 0:
                return
            
            for i in range(idx, len(candidates)):
                if candidates[i] > tar:
                    return
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                explore(path, tar - candidates[i], i + 1)
                path.pop()
        
        explore([], target, 0)

        return rslt