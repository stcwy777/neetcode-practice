class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {v: i for i,v in enumerate(nums, start=0)}

        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)
        for num in nums:
            if num in hash_map and (target - num) in hash_map:
                if num * 2 == target:
                    if len(hash_map[num]) > 1:
                        return hash_map[num]
                    else:
                        continue
                else:
                    return hash_map[num] + hash_map[target - num]
