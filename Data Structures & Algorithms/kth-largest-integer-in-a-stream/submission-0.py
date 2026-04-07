class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._hq = nums
        heapq.heapify(self._hq)
        self._k = k


    def add(self, val: int) -> int:
        heapq.heappush(self._hq, val)

        for i in range(len(self._hq) - self._k):
            heapq.heappop(self._hq)
        return self._hq[0]