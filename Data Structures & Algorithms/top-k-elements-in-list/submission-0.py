class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        TopK = []

        for num, freq in freq.items():
            heapq.heappush(TopK, (freq, num))
        
        while len(TopK) > k:
            heapq.heappop(TopK)
        
        return [i[1] for i in TopK]