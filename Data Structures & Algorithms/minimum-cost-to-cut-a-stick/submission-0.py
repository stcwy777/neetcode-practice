from functools import cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        # dp = [[0] * n for _ in range(n)]

        @cache
        def dfs(i: int, j: int) -> int:
            if  j <= i + 1:
                return 0

            return min(dfs(i, k) + dfs(k, j) for k in range(i + 1, j)) + cuts[j] - cuts[i]

        return dfs(0, len(cuts) - 1)


