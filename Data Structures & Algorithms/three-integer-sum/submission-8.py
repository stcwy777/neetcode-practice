class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        rslt = set()
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = N - 1

            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    rslt.add((nums[i], nums[j], nums[k]))
                    # rslt.add([i, j, k])
                    j += 1
                elif  nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return list(rslt)
