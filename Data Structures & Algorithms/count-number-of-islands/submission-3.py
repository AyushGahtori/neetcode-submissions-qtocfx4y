class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if we ever find one island += 1
        # inside helper ever find one make it 0

        ROWS, COLS = len(grid), len(grid[0])

        island = 0

        def helper(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return

            if grid[r][c] == "1":
                grid[r][c] = "0"    

            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    island += 1
                    helper(r, c)


        return island