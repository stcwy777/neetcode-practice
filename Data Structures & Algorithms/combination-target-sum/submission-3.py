class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        rslt = []
        nums.sort()

        def explore(path: List[int], idx: int, total: int):

            if target == total:
                rslt.append(path.copy())
                return
            
            for i in range(idx, len(nums)):
                if nums[i] + total > target:
                    return
                path.append(nums[i])
                explore(path, i, total + nums[i])
                path.pop()
        
        explore([], 0, 0)
        return rslt
