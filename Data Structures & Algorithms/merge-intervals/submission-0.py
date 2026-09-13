class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        n = len(intervals)

        i = 0

        while i < n - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])
                i += 1
            else:
                intervals[i + 1][0] = intervals[i][0] 
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
                i += 1

        res.append(intervals[i])

        return res


