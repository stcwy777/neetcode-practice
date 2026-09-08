from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""
        
        countT = Counter(t)
        totalT = len(countT.keys())
        min_len = float('INF')
        
        
        l = 0
        while l < len(s):
            if s[l] not in countT:
                l += 1
            else:
                break
        r, start = l, l
        while r < len(s):

            if s[r] in countT:
                countT[s[r]] -= 1
                if countT[s[r]] == 0:
                    totalT -= 1
                # print(l, r, countT, totalT)
                if totalT == 0:
                    # print(l, r, countT)                  
                    while (r - l + 1) >= len(t):
                        if s[l] not in countT:

                            l += 1
                        elif countT[s[l]] < 0:
                            countT[s[l]] += 1
                            l += 1
                        else:
                            if min_len > (r - l + 1):
                                start = l
                                min_len = r - l + 1
                            break
        
            r += 1
        
        return "" if min_len == float('INF') else s[start:start + min_len]



