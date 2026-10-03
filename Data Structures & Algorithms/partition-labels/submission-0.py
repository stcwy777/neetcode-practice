class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        labels = {}
        for i in range(len(s)):
            if s[i] not in labels:
                labels[s[i]] = [i, i]
            else:
                labels[s[i]][1] = i
        
        intervals = list(labels.values())

        intervals.sort(key=lambda x:x[0])

        left, right = intervals[0]

        for i in range(1, len(intervals)):
            if left < intervals[i][0] < right:
                right = max(right, intervals[i][1])
            else:
                res.append(right - left + 1)
                left, right = intervals[i]
        res.append(right - left + 1)
        return res