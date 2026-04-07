class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold

        cur_sum = sum(arr[:k])
        counts = 0
        if cur_sum >= target:
            counts = 1
        for i in range(len(arr) - k):
            cur_sum += (arr[i + k] - arr[i])
            if cur_sum >= target:
                counts += 1
        return counts