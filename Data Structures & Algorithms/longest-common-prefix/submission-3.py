class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        if len(base) == 0:
            return ""
        for i in range(len(base)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or base[i] != strs[j][i]:
                    return base[0:i]
        
        return base[:i + 1]