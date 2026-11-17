"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = [] 
        heapq.heapify(heap)
        rooms = 0

        for interval in intervals:
            start = interval.start
            end = interval.end

            if not heap or heap[0] > start:
                heapq.heappush(heap, end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
        
        return len(heap)
