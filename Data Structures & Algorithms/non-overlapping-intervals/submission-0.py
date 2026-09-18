class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        tail = intervals[0]
        remove = 0
        for i in range(1, n):
            cur  = intervals[i]
            if tail[1] <= cur[0]:
                tail = cur
            else:
                remove += 1
            
        return remove