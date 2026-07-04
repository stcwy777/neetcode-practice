class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        bag = total // 2
        N = len(stones)

        dp = [[0] * (bag + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, bag + 1):
                cur_weight = stones[i - 1]
                if cur_weight <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_weight)
                else:
                    dp[i][j] = dp[i - 1][j]
        
        best = dp[N][bag]

        return total - 2 * best