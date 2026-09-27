class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key=lambda x:x[0])
        sort_queries = [(x[1], x[0]) for x in enumerate(queries)]
        sort_queries.sort(key=lambda x:x[0])

        candidates = []
        heapq.heapify(candidates)
        res = [-1] * len(queries)
        i = 0

        for q, idx in sort_queries:
            
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(candidates, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while candidates and candidates[0][1] < q:
                heapq.heappop(candidates)
            
            if len(candidates):
                res[idx] = candidates[0][0]

        return res