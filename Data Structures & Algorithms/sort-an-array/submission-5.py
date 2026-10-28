import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(s: int, e: int) -> None:
            if e - s + 1 <= 1:
                return

            rand_idx = random.randint(s, e)
            nums[rand_idx], nums[e] = nums[e], nums[rand_idx]

            pivot = nums[e]
            left = s

            for i in range(s, e):
                if nums[i] < pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1

            nums[left], nums[e] = nums[e], nums[left]

            quicksort(s, left - 1)
            quicksort(left + 1, e)

        quicksort(0, len(nums) - 1)
        return nums