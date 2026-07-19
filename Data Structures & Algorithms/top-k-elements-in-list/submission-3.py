class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        topK = []

        for num, count in freq.items():
            if len(topK) < k:
                heapq.heappush(topK, (count, num))
            else:
                heapq.heappushpop(topK, (count, num))
        
        return [i[1] for i in topK]