class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = True
            else:
                return True
        return False