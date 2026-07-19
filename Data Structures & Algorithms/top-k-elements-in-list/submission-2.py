class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        topK = []

        for num, count in freq.items():
            heapq.heappush(topK, (count, num))
            if len(topK) > k:
                heapq.heappop(topK)
        
        return [i[1] for i in topK]