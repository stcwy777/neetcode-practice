class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        # for i in range(len(s) - 1):
        #     score += abs(ord(s[i+1]) - ord(s[i]))
        score = sum([abs(ord(a)- ord(b)) for a, b in zip(s, s[1:])])
        return score
