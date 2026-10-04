class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_pos = {s[i]:i for i in range(len(s))}

        res = []

        start = 0
        end = 0
        for i in range(len(s)):

            end = max(end, last_pos[s[i]])

            if end == i:
                res.append(end - start + 1)
                start = i + 1
        
        return res