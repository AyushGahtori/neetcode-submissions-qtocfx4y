class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])    
        island = 0
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visit):
                return
            visit.add((r, c))  # we can use a for loop here but that makes things more complicates
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit: # if this condition is true it means we found a new island
                    # we cannot switch the order of these two lines because
                    # if we run dfs first it will marks all the connected 1 as visited and then
                    # the condition will not pass 
                    island += 1 # we update our no of island 
                    dfs(r, c) # then we run the dfs on that island all mark all the connected 1 as visited  
        return island               

        