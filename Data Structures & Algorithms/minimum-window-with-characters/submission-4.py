class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        check = {}
        for c in t:
            check[c] = check.get(c, 0) + 1
        needs = len(check.values())

        l = 0
        while l < len(s) and s[l] not in check:
            l += 1
        
        min_len = float('inf')
        for r in range(l, len(s)):
            if s[r] in check:
                check[s[r]] -= 1
                if check[s[r]] == 0:
                    needs -= 1

                if needs == 0:
                    while s[l] not in check or check[s[l]] < 0:
                        if s[l] in check:
                            check[s[l]] += 1
                            l += 1
                        elif s[l] not in check:
                            l += 1
                    
                    if (r - l + 1) < min_len:
                        start = l
                        min_len = r - l + 1

        return "" if min_len == float('inf') else s[start:start + min_len]



