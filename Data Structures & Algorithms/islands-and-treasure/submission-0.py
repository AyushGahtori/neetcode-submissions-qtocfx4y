# grid[r][c] = dist replacing the current value of this place to the distance of it from a gate
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (r < 0 or c < 0 or r >= rows or c>= cols or (r, c) in visit or grid[r][c] == -1):
                return # stops the loop
            q.append([r, c])
            visit.add((r, c))    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dist = 0            
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)   
            dist += 1                 

        
        
        