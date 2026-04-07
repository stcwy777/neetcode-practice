class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, max_len = 0, 0
        sub_str = {}

        for R in range(len(s)):
            if s[R] not in sub_str:
                sub_str[s[R]] = R
            else:
                max_len = max(R - L, max_len)
                for i in range(L, sub_str[s[R]]):
                    del sub_str[s[i]]
                
                L = sub_str[s[R]] + 1
                sub_str[s[R]] = R

        max_len = max(max_len, len(sub_str))
        return max_len