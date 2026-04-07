class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rslt = []
        #Helper
        def explore(path: List[int], tar: int, idx: int):

            if idx >= len(nums) or tar < 0:
                return
            elif tar == 0:
                rslt.append(path.copy())
                return
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                explore(path, tar - nums[i], i)
                path.pop()
        
        explore([], target, 0)
        return rslt