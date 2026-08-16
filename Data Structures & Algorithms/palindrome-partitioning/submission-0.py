class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rslt = []
        path = []

        N = len(s)
        pal = [[False] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        def dfs(start: int) -> None:
            if start == len(s):
                rslt.append(path[:])
                return
            
            for i in range(start, N):
                if pal[start][i]:
                    path.append(s[start:i + 1])
                    dfs(i + 1)
                    path.pop()
        dfs(0)        
        return rslt
