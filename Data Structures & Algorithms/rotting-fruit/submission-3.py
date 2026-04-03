from collections import deque

class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh = 0

        # Initialize
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Helper function
        def helper(r, c):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                grid[r][c] == 0 or 
                (r, c) in visited):
                return
            
            visited.add((r, c))
            if grid[r][c] == 1:
                grid[r][c] = 2
                nonlocal_fresh[0] -= 1
            
            q.append((r, c))

        time = 0
        nonlocal_fresh = [fresh]  # trick to modify inside helper

        while q and nonlocal_fresh[0] > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                helper(r + 1, c)
                helper(r - 1, c)
                helper(r, c + 1)
                helper(r, c - 1)
            time += 1

        return time if nonlocal_fresh[0] == 0 else -1
