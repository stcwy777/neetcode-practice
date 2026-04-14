class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0
        max_char = s[0]
        freq = {s[0]: 1}
        max_freq = 1
        max_len = 1

        for R in range(1, len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1

            if max_freq < freq[s[R]]:
                max_freq = freq[s[R]]
                max_char = s[R]

            if (R - L + 1 - k) > max_freq:
                freq[s[L]] -= 1
                if s[L] == max_char:
                    max_freq -= 1                
                L += 1
            else:
                max_len = max(max_len, R - L + 1)

        return max_len
