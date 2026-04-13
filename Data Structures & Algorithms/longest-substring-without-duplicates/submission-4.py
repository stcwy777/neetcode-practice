class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        curLen = 1
        if not s:
            return 0
        dup = {s[L]: 0}
        maxLen = 0
        for R in range(1, len(s)):
            if s[R] not in dup:
                curLen += 1
                dup[s[R]] = R
            else:
                maxLen = max(maxLen, curLen)
                newL = dup[s[R]] + 1
                curLen = R - dup[s[R]]
                for i in range(L, newL):
                    del dup[s[i]]
                dup[s[R]] = R
                L = newL

        maxLen = max(maxLen, curLen)
        return maxLen