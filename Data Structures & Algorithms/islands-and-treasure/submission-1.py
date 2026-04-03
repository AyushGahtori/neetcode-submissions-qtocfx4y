class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0]) # get the len of column and rows
        visit = set()
        q = deque()

        def addCell(r, c):
            # all the base cases.
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
            # we are gonna pop the gates in the first itteration from the q because its the only thing they have
            for i in range(len(q)): # in the first intteration its just gonna have the coordination of the gates.
            # then in second itteraton its gonna have the coordinates of the 1s then they are gonna pop and then we go on and on.
                r, c = q.popleft()

                # we are still putiing it inside this loop because
                # after all the gate there are gonna be all the room which are one distance away in the q.
                # this is not gonna modify the value of the gates.
                grid[r][c] = dist # grid[r][c] = dist replacing the current value of this place to the distance of it from a gate
                addCell(r + 1, c)
                addCell(r - 1, c) # check all the direction.
                addCell(r, c + 1)
                addCell(r, c - 1)   
            dist += 1 # increment after every layer        

        
        
        