class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for char in set(s):
            L = 0
            changes = 0
            for R in range(len(s)):
                if s[R] != char:
                    changes += 1
                if changes > k:
                    if s[L] != char:
                        changes -= 1
                    L += 1
                max_len = max(max_len, R - L + 1)
        return max_len