class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW, COL = len(text1), len(text2)

        pre = [0] * (COL + 1)
        cur = [0] * (COL + 1)
        for i in range(1, ROW + 1):
            cur = [0] * (COL + 1)
            for j in range(1, COL + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur[j] = pre[j - 1] + 1
                else:
                    cur[j] = max(pre[j], cur[j - 1])
            pre = cur.copy()
        
        return cur[COL]