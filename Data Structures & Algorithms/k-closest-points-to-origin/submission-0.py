class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_size = len(points) - k
        min_heap = []
        heapq.heapify(min_heap)
        rslt = []
        dist_map = {}
        for p in points:
            eucli_dist = math.sqrt((p[0] - 0.0)**2 + (p[1] - 0.0)**2)

            if eucli_dist not in dist_map:
                dist_map[eucli_dist] = [p]
            else:
                dist_map[eucli_dist].append(p)
            
            heapq.heappush(min_heap, eucli_dist)

            if len(min_heap) > heap_size:
                rslt.append(dist_map[heapq.heappop(min_heap)].pop())
        return rslt