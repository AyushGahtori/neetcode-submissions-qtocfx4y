class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get the length and width of the board
        row, col = len(board), len(board[0])
        # we do not want to visit the same character twice so we ar gonna use a set
        path = set()

        def dfs(r, c, i): # r, c = our current co-ordinates and i to treverse into the word.
            #base cases

            # we found the desierd word.
            if i == len(word):
                return True
            if (r < 0 or c < 0 or # out of bound
                r>= row or c>=col or # out of bound
                word[i] != board[r][c] or # we are at the wrong character.
                (r, c) in path): # we are visiting a character we alredy visited.
                return False
                
                # this implies that the co-ordinates we are currently at
                # matches the word(i) character so we add it into the path.
            path.add((r, c))

            res = (dfs(r + 1, c, i + 1) or # look down
                   dfs(r - 1, c, i + 1) or # look up
                   dfs(r, c + 1, i + 1) or # look forword
                   dfs(r, c - 1, i + 1))   # look backword

            path.remove((r, c)) # remove the position we just added
            return res 

        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0): # if the ever return True
                    return True
        return False            





        