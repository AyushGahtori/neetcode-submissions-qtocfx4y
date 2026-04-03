class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # This initializes pac and atl, which will store cells that can reach the
                                # Pacific and Atlantic oceans, respectively.

        def dfs(r, c, visit, prevHeight):

            # prevHeight: prevHeight ensures that we only move to cells where the height is greater than or equal
            # to the previous cell’s height. It prevents moving "upwards" in height, simulating water flow.
            if (
                (r, c) in visit # This checks if we’ve already visited this cell for the current DFS, preventing reprocessing.
                or r < 0 # This checks if the cell is out of bounds.
                or c < 0 # This checks if the cell is out of bounds.
                or r == ROWS # This checks if the cell is out of bounds.
                or c == COLS # This checks if the cell is out of bounds.
                or heights[r][c] < prevHeight # This checks if the next cell is lower than the current cell.
                                              # Water can’t flow “up” to a cell with a lower height, so if the condition is met, the function stops recursion.
            ):
                return # stops recursion if we are out of bound or cell already processed or the hight requrment dont fullfill.
            visit.add((r, c)) # visit is either pac or atl depending upon who called the function from call 1, 2, 3, 4
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS): # loop for the first and last columns
            dfs(0, c, pac, heights[0][c]) # call 1
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # call 2

        for r in range(ROWS): # loop for the first and last rows
            dfs(r, 0, pac, heights[r][0]) # call 3
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # call 4

        res = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl: # if this certain position is in both set then its comun so apppend it to the list.
                    res.append([r, c])
        return res
