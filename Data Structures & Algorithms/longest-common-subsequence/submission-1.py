class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW, COL = len(text1), len(text2)

        S = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for i in range(1, ROW + 1):
            for j in range(1, COL + 1):
                if text1[i - 1] == text2[j - 1]:
                    S[i][j] = S[i - 1][j - 1] + 1
                else:
                    S[i][j] = max(S[i][j - 1], S[i - 1][j])
        
        return S[ROW][COL]