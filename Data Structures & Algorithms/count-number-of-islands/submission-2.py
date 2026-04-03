class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if not grid:
            return 0
        hashset = set()    
        ROWS, COLS = len(grid), len(grid[0])

        def backtrack(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in hashset or grid[r][c] == "0":
                return 

            grid[r][c] == "0"
            hashset.add((r, c))
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in hashset:
                    backtrack(r, c)
                    island += 1
        return island            
        