class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        def bfs(r, c):
            # Ensure we first check for in-bounds indices before accessing grid[r][c]
            if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == 1:
                grid[r][c] = 2  # Make the fresh orange rotten
                q.append([r, c])  # Add the newly rotten orange to the queue
                return True
            return False    

        # Initialize queue with all initially rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        # Process the grid while we have oranges to rot and fresh oranges remaining
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # Try to rot the adjacent cells
                if bfs(r + 1, c): fresh -= 1
                if bfs(r - 1, c): fresh -= 1
                if bfs(r, c + 1): fresh -= 1
                if bfs(r, c - 1): fresh -= 1
            time += 1   

        # Return the time if no fresh oranges are left, otherwise -1
        return time if fresh == 0 else -1   
