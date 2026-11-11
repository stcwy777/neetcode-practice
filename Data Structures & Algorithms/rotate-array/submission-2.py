class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(l: int, r: int, array: List[int]) -> None:

            while l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1
        
        reverse(0, n - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, n - 1, nums)

        return