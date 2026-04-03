class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(pos):
            if pos >= len(cost):
                return 0
            if pos in memo:
                return memo[pos]
            memo[pos] = cost[pos] + min(dfs(pos + 1), dfs(pos + 2))
            return memo[pos]

        return min(dfs(0), dfs(1))          