class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # our approch is pritty simple we first convert all bordering O into an T
        # via a capture function that look all four directions and precess all the O that indirectly borders the border.
        # then we just run a double for loop to convert remaning O to an X.
        # then at last we convert all the T back into an O


        # we do need the capture function because if a O borders another O that border the border the first O will still be an O
        # and should not be converted into an X
        # for example ["X","X","X","X"]
        #             ["X","O","O","X"]
        #             ["X","O","O","X"]
        #             ["X","O","X","X"]

        # the output will be the same as input exactly same because
        # every O borders the border indirectly because of the O in the last column.


        rows, cols = len(board), len(board[0])

        # phase 1 convert the bordering O into an T:
        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"): # if you think you can remove board[r][c] != "O" from here
                                                                                 # you cant this check is for checking neighbours fool.
                return # stops the backtracking
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        # phase 2 convert all the remaning O to an X:

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # phase 3 convert the T back into "O"            

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"                    
