class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        uniPerms = []
        used = [False] * len(nums)

        def dfs(perm: List[int]) -> None:
            if len(perm) == len(nums):
                uniPerms.append(perm[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                elif i >= 1 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                else:
                    used[i] = True
                    perm.append(nums[i])
                    dfs(perm)
                    perm.pop()
                    used[i] = False
        
        dfs([])

        return uniPerms