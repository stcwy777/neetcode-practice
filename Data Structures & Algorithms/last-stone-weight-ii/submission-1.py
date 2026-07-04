class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        bag = total // 2
        N = len(stones)

        dp = [0] * (bag + 1)

        for i in range(1, N + 1):
            cur_row = [0] * (bag + 1)
            cur_weight = stones[i - 1]

            for j in range(1, bag + 1):
                if cur_weight <= j:
                    cur_row[j] = max(dp[j], dp[j - cur_weight] + cur_weight)
                else:
                    cur_row[j] = dp[j]
            dp = cur_row
        
        best = dp[bag]

        return total - 2 * best