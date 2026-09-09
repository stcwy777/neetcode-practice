class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        comb = []
        res = []
        nums.sort()

        def dfs(start: int, tar: int) -> None:
            if tar < 0 or start >= n:
                return
            elif tar == 0:
                res.append(comb[:])
            
            for i in range(start, n):
                if nums[i] > tar:
                    break
                comb.append(nums[i])
                dfs(i, tar - nums[i])
                comb.pop()
            return
        
        dfs(0, target)

        return res