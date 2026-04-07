class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        target = k * threshold

        for i in range(len(arr) - k + 1):
            if sum(arr[i:i + k]) >= target:
                count += 1
        return count